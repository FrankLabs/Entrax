from django.shortcuts import render_to_response, RequestContext
from apps.rider.forms import ProfileRiderForm


def prueba(request):
    form = ProfileRiderForm()
    if request.method == 'POST':
        form = ProfileRiderForm(request.POST)
        if form.is_valid():
            form.save()
    return render_to_response(
        'prueba.html',
        RequestContext(
            request,
            {
                'form': form
            }
        ),
    )
