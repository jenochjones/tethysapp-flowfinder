from django.shortcuts import render
from tethys_sdk.permissions import login_required
from django.http import JsonResponse, HttpResponse

import requests

@login_required()
def home(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'flowfinder/home.html', context)


def get_wms_images(request):
    try:
        if 'main_url' in request.GET:
            request_url = request.GET.get('main_url')
            query_params = request.GET.dict()
            query_params.pop('main_url', None)
            # old_dodsrcfile, old_netrc = set_rc_vars()
            r = requests.get(request_url, params=query_params)
            # reset_rc_vars(old_dodsrcfile, old_netrc)
            return HttpResponse(r.content, content_type="image/png")
        else:
            return JsonResponse({})
    except Exception as e:
        print(e)
        return JsonResponse({'error': e})
