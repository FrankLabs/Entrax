from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response(
        'core/home.html',
        RequestContext(
            request,
            {
                'mi_nombre': 'Pab   lo Dalmasso',
            }
        )
    )
