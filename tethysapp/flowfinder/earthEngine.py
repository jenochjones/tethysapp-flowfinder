from django.http import JsonResponse, HttpResponse
import json
import pandas as pd
from datetime import datetime

from .gee.methods import get_elevation_image, get_data_image, get_time_series, aggregate_to_daily
from .gee.products import EE_PRODUCTS


def get_data_tiles(request):
    try:
        product = request.GET.get('product')
        dataset = request.GET.get('dataset')
        elevation_url = get_data_image(product, dataset)
        array_to_return = {
            'data': elevation_url
        }
        return JsonResponse(array_to_return)
    except Exception as e:
        array_to_return = {
            'errorMessage': 'There was an error while getting the elevations.',
            'error': str(e)
        }
        return JsonResponse(array_to_return)


def get_elevation_tiles(request):
    try:
        product = request.GET.get('product')
        dataset = request.GET.get('dataset')
        elevation_url = get_elevation_image(product, dataset)
        array_to_return = {
            'data': elevation_url
        }
        return JsonResponse(array_to_return)
    except Exception as e:
        array_to_return = {
            'errorMessage': 'There was an error while getting the elevations.',
            'error': str(e)
        }
        return JsonResponse(array_to_return)


def plot_time_series(request):
    try:
        product = request.POST.get('product')
        dataset = request.POST.get('dataset')
        first_date = request.POST.get('firstDate')
        date_from = datetime.strftime(datetime.strptime(first_date, '%Y-%m-%d'), '%Y-%m-%dT%H:%M:%S')
        second_date = request.POST.get('secondDate')
        date_to = datetime.strftime(datetime.strptime(second_date, '%Y-%m-%d'), '%Y-%m-%dT%H:%M:%S')
        geojson_geometry = json.loads(request.POST.get('geojson'))
        daily = request.POST.get('daily')
        get_all = request.POST.get('allProducts')

        if get_all == 'true':
            time_series = get_time_series('ECMWF_ERA5_DAILY', 'total_precipitation', geojson_geometry, date_from,
                                          date_to)

            for each_dataset in EE_PRODUCTS['GLDAS2_1']:
                sub_time_series = aggregate_to_daily('GLDAS2_1', each_dataset, geojson_geometry, date_from, date_to)
                time_series[each_dataset] = sub_time_series[each_dataset]

        else:
            if daily == 'false':
                time_series = get_time_series(product, dataset, geojson_geometry, date_from, date_to)
            else:
                time_series = aggregate_to_daily(product, dataset, geojson_geometry, date_from, date_to)

        array_to_return = {
            'data': time_series
        }
        return JsonResponse(array_to_return)
    except Exception as e:
        print(e)
        array_to_return = {
            'errorMessage': 'There was an error while getting the elevations.',
            'error': str(e)
        }
        return JsonResponse(array_to_return)
