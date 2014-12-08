from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from apps.championship.models import Championship, DISCIPLINE_CHOICES
from django.contrib.auth.decorators import login_required


def hola_mundo(request, nombre=None):
    """
    is not es igual a !=
    pero se usa para decir que no es Nulo
    """
    if nombre is not None:
        respuesta = 'Hola ' + nombre
    else:
        respuesta = 'Hola Mundo.'
    return HttpResponse(respuesta)


@login_required
def championship_list(request, discipline_parametro=None):
    championship_lst = Championship.objects.all()
    if discipline_parametro is not None:
        championship_lst = championship_lst.filter(
            discipline=discipline_parametro
        )
    return render_to_response(
        'championship/list.html',
        RequestContext(
            request,
            {
                'list': championship_lst,
                'discipline': DISCIPLINE_CHOICES,
                'discipline_parametro': discipline_parametro
            }
        )
    )
