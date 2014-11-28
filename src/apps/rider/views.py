from django.shortcuts import render

from apps.rider.forms import NewRiderForm

def new_rider(request):
    if request.method == 'POST':
        # Si se ingresaron datos
        form = NewRiderForm(request.POST)
        if form.is_valid():
            # Si los datos son correctos se guardan en la base de datos
            form.save(commit=True)
        return render(request, 'new_rider.html', {'form': form,})
    else:
        # Si hay un GET se muestra el formulario
        form = NewRiderForm()
        return render(request, 'new_rider.html', {'form': form,})
