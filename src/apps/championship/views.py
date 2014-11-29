from django.shortcuts import render, HttpResponse
from apps.championship.models import Championship, DISCIPLINE_CHOICES


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


def championship_list(request, discipline_parametro=None):
    championship_lst = Championship.objects.all()
    if discipline_parametro is not None:
        championship_lst = championship_lst.filter(
            discipline=discipline_parametro
        )
    resultado = '<table border="1">'
    resultado += '<thead>'
    resultado += '<tr>'
    resultado += '<td>Disciplina</td>'
    resultado += '<td>Nombre</td>'
    resultado += '<td>Lugar</td>'
    resultado += '</tr>'
    resultado += '</thead>'
    resultado += '<tbody>'
    for item in championship_lst:
        resultado += '<tr>'
        resultado += '<td>'
        resultado += str(item.get_discipline_display())
        resultado += '</td>'
        resultado += '<td>'
        resultado += item.name
        resultado += '</td>'
        resultado += '<td>'
        resultado += item.place.name
        resultado += '</td>'
        resultado += '</tr>'
    resultado += '</tbody>'
    resultado += '</table><br>'
    resultado += '<h2>Filtos:</h2>'
    for x in DISCIPLINE_CHOICES:
        resultado += '<p><a href="/championship_list/'
        resultado += str(x[0])
        resultado += '/">'
        resultado += str(x[1])
        resultado += '</a></p>'
    resultado += '<p><a href="/championship_list/">All</a>'
    return HttpResponse(resultado)
