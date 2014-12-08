from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm


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


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            return home(request)
    return render_to_response(
        'registration/signup.html',
        RequestContext(
            request,
            {
                'form': form,
            }
        )
    )
