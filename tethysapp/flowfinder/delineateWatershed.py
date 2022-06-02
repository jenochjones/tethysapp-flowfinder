from django.http import JsonResponse, HttpResponse
from pysheds.grid import Grid
from area import area
from .gee.products import EE_PRODUCTS

import elevation
import os
import json
import fiona
import geopandas
import geojson
import ee
import requests
import numpy as np


def download_ee_elevation(request):
    bounds = json.loads(request.GET.get('bounds'))
    product = request.GET.get('product')
    dataset = request.GET.get('dataset')
    path_to_dem = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'workspaces', 'app_workspace', 'elevation.tif')

    ee_product = EE_PRODUCTS[product][dataset]
    collection_name = ee_product['collection']
    band = ee_product.get('band', None)
    accumulation_value = ee_product.get('accumulation', None)

    ee_geometry = ee.Geometry.BBox(bounds['_southWest']['lng'], bounds['_southWest']['lat'],
                                   bounds['_northEast']['lng'], bounds['_northEast']['lat'])
    elevation_image = ee.Image(collection_name)

    download_url = elevation_image.getDownloadURL({
        'bands': [band, ],
        'region': ee_geometry,
        'format': 'GEO_TIFF'
    })

    response = requests.get(download_url)
    with open(path_to_dem, 'wb') as f:
        f.write(response.content)

    streams = generate_streams(path_to_dem, accumulation_value)
    dict_to_return = {
        'data': {
            'streams': streams
        }
    }

    return JsonResponse(dict_to_return)


def download_elevation(request):
    bounds = json.loads(request.POST.get('bounds'))
    path_to_dem = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'workspaces', 'app_workspace', 'elevation.tif')
    bounds_formatted = (bounds['_southWest']['lng'], bounds['_southWest']['lat'], bounds['_northEast']['lng'], bounds['_northEast']['lat'])

    elevation.clip(bounds=bounds_formatted, output=path_to_dem, product='SRTM3')
    elevation.clean()

    streams = generate_streams(path_to_dem)
    dict_to_return = {
        'data': {
            'streams': streams
        }
    }

    return JsonResponse(dict_to_return)


def generate_streams(path_to_elevation, accumulation_value):
    grid = Grid.from_raster(path_to_elevation)
    dem = grid.read_raster(path_to_elevation)
    pit_filled_dem = grid.fill_pits(dem)
    flooded_dem = grid.fill_depressions(pit_filled_dem)
    inflated_dem = grid.resolve_flats(flooded_dem)
    flow_direction = grid.flowdir(inflated_dem)
    accumulation = grid.accumulation(flow_direction)
    branches = grid.extract_river_network(flow_direction, accumulation > accumulation_value)
    return branches


def delineate_watershed(request):
    coords = json.loads(request.POST.get('coords'))
    path_to_dem = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'workspaces', 'app_workspace', 'elevation.tif')

    path_to_shapefile = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                     'workspaces', 'app_workspace', 'catchment.shp')

    path_to_geojson = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                     'workspaces', 'app_workspace', 'catchment.geojson')

    grid = Grid.from_raster(path_to_dem)
    dem = grid.read_raster(path_to_dem)
    pit_filled_dem = grid.fill_pits(dem)
    flooded_dem = grid.fill_depressions(pit_filled_dem)
    inflated_dem = grid.resolve_flats(flooded_dem)
    flow_direction = grid.flowdir(inflated_dem)
    accumulation = grid.accumulation(flow_direction)

    x_snap, y_snap = grid.snap_to_mask(accumulation > 100, (coords['lng'], coords['lat']))
    catch = grid.catchment(x=x_snap, y=y_snap, fdir=flow_direction)
    grid.clip_to(catch)
    shapes = grid.polygonize()

    elevations_in_catchment = np.multiply(dem, catch)
    number_of_nonzero = np.count_nonzero(elevations_in_catchment)
    avg_elevation = float(np.sum(elevations_in_catchment) / number_of_nonzero)

    schema = {
        'geometry': 'Polygon',
        'properties': {'LABEL': 'float:16', 'AVG_ELEV': 'float:16'}
    }

    with fiona.open(path_to_shapefile, 'w',
                    driver='ESRI Shapefile',
                    crs=grid.crs.srs,
                    schema=schema) as c:
        i = 0
        for shape, value in shapes:
            rec = {}
            rec['geometry'] = shape
            rec['properties'] = {
                'LABEL': str(value),
                'AVG_ELEV': avg_elevation
                                 }
            rec['id'] = str(i)
            c.write(rec)
            i += 1

    shapefile = geopandas.read_file(path_to_shapefile)
    shapefile.to_file(path_to_geojson, driver='GeoJSON')

    watershed = geopandas.read_file(path_to_geojson)
    watershed_proj = watershed['geometry'].to_crs({'proj': 'cea'})
    watershed_area = watershed_proj.area[0]

    watershed['AREA'] = float(watershed_area)
    watershed.to_file(path_to_geojson, driver='GeoJSON')

    with open(path_to_geojson) as geojson_file:
        watershed_geojson = geojson.load(geojson_file)

    dict_to_return = {
        'data': {
            'watershed': watershed_geojson
        }
    }

    return JsonResponse(dict_to_return)
