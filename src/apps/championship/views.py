from django.shortcuts import render

from apps.championship.forms import ChampionshipInscriptionForm

def inscription(request):
    if request.method == 'POST':
        # Si se ingresaron datos
        form = ChampionshipInscriptionForm(request.POST)
        if form.is_valid():
            # Si los datos son correctos se guardan en la base de datos
            form.save(commit=True)
        return render(request, 'champ_inscription.html', {'form': form,})
    else:
        # Si hay un GET se muestra el formulario
        form = ChampionshipInscriptionForm()
        return render(request, 'champ_inscription.html', {'form': form,})
