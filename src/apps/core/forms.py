from django.forms import ModelForm
from apps.core.models import Country, State, Citie


class CountryForm(ModelForm):

    class Meta:
        model = Country

class StateForm(ModelForm):

    class Meta:
        model = State

        fields = {
            'name', 'country'
        }

class CitieForm(ModelForm):

    class Meta:
        model = Citie

        fields = {
            'name', 'state'
        }