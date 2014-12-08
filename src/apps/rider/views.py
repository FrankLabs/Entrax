from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect

from apps.rider.forms import ProfileRiderForm
from apps.core.models import Country, State, Citie


def prueba(request, country=None, state=None):
    state_lst = []
    citie_lst = []
    country_lst = Country.objects.all()
    
    if country is not None:
        state_lst = State.objects.filter(
            country=country
        )

    if state is not None:
        citie_lst = Citie.objects.filter(
            state=state
        )

    form = ProfileRiderForm()

    if request.method == 'POST':
        form = ProfileRiderForm(request.POST)
        if form.is_valid():
            print 'HOLA'
            rider = form.save(commit=False)
            return HttpResponseRedirect('/')


    return render_to_response(
        'prueba.html',
        RequestContext(
            request,
            {
                'form': form,
                'country_lst': country_lst,
                'state_lst': state_lst,
                'citie_lst': citie_lst
            }
        ),
    )
