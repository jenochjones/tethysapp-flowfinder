import ee
import pandas as pd

from .products import EE_PRODUCTS

service_account = 'enoch-01@flowfinder-01.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, '/Users/jonjones/.tethys/workspaces/flowfinder/app_workspace/flowfinder-01-3a1a6998d916.json')
ee.Initialize(credentials)


def image_to_map_id(image_name, vis_params={}):
    """
    Get map_id parameters
    """
    try:
        ee_image = ee.Image(image_name)
        map_id = ee_image.getMapId(vis_params)
        tile_url = map_id['tile_fetcher'].url_format
        return tile_url

    except Exception as e:
        print('An error occurred while attempting to retrieve the map id.')
        print(e)


def get_elevation_image(product, dataset):
    """
    Get tile url for image collection asset.
    """

    ee_product = EE_PRODUCTS[product][dataset]
    collection = ee_product['collection']
    band = ee_product.get('band', None)
    vis_params = ee_product.get('vis_params', {})

    try:
        ee_image = ee.Image(collection)
        if band:
            ee_image = ee_image.select(band)
        tile_url = image_to_map_id(ee_image, vis_params)
        return tile_url

    except Exception as e:
        print('An error occurred while attempting to retrieve the image collection asset.')
        print(e)


def get_data_image(product, dataset, reducer='median'):
    """
    Get tile url for image collection asset.
    """

    ee_product = EE_PRODUCTS[product][dataset]
    collection = ee_product['collection']
    band = ee_product.get('band', None)
    vis_params = ee_product.get('vis_params', {})
    date = ee_product.get('date', '2022-01-02T03:00:00Z')

    try:
        ee_collection = ee.ImageCollection(collection)
        if band:
            ee_collection = ee_collection.select(band)
        if date:
            ee_filter_date = ee.Filter.date(date)
            ee_collection = ee_collection.filter(ee_filter_date)
        if reducer:
            ee_collection = getattr(ee_collection, reducer)()
        tile_url = image_to_map_id(ee_collection, vis_params)
        return tile_url

    except Exception as e:
        print('An error occurred while attempting to retrieve the image collection asset.')
        print(e)


def aggregate_to_daily(product, dataset, geometry, date_from, date_to, scale=30, reducer='mean'):
    print('starting aggregation')

    ee_product = EE_PRODUCTS[product][dataset]
    collection_name = ee_product['collection']
    band = ee_product.get('band', None)

    try:
        ee_geometry = ee.Geometry.Polygon(geometry['features'][0]['geometry']['coordinates'])
        ee_date_from = ee.Date(date_from)
        ee_date_to = ee.Date(date_to)

        collection = ee.ImageCollection(collection_name)

        def to_average(day_number):
            start = ee_date_from.advance(day_number, 'days')
            end = start.advance(21, 'hours')
            single_day = collection.filterDate(start, end).select(band)
            average_of_day = single_day.mean()

            the_reducer = getattr(ee.Reducer, reducer)()
            index_value = average_of_day.reduceRegion(the_reducer, ee_geometry, scale).get(band)

            date_string = start.format('YYYY-MM-dd:HH-mm-ss')
            index_image = ee.Image().set('indexValue', [date_string, index_value])

            return index_image

        number_of_days = ee_date_to.difference(ee_date_from, 'days')
        day_list = ee.List.sequence(0, number_of_days.subtract(1))

        daily_average = ee.ImageCollection(day_list.map(to_average))

        index_collection_agg = daily_average.aggregate_array('indexValue')

        values = index_collection_agg.getInfo()
        time_series = pd.DataFrame(values, columns=['datetime', band])

    except Exception as e:
        print('An error occurred while attempting to retrieve the time series.')
        print(e)

    return time_series


def get_time_series(product, dataset, geometry, date_from, date_to, scale=30, reducer='mean'):
    ee_product = EE_PRODUCTS[product][dataset]
    collection_name = ee_product['collection']
    band = ee_product.get('band', None)

    try:
        ee_geometry = ee.Geometry.Polygon(geometry['features'][0]['geometry']['coordinates'])
        ee_date_from = ee.Date(date_from)
        ee_date_to = ee.Date(date_to)
        collection = ee.ImageCollection(collection_name).filterDate(ee_date_from, ee_date_to).select(band)

        def get_index(image):
            the_reducer = getattr(ee.Reducer, reducer)()
            index_value = image.reduceRegion(the_reducer, ee_geometry, scale).get(band)
            date_string = image.date().format('YYYY-MM-dd:HH-mm-ss')
            index_image = ee.Image().set('indexValue', [date_string, index_value])
            return index_image

        index_collection = collection.map(get_index)
        index_collection_agg = index_collection.aggregate_array('indexValue')
        values = index_collection_agg.getInfo()
        time_series = pd.DataFrame(values, columns=['datetime', band])

    except Exception as e:
        print('An error occurred while attempting to retrieve the time series.')
        print(e)

    return time_series
