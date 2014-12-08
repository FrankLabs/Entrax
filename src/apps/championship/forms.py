from django.forms import ModelForm, TextInput, DateInput
from apps.championship.models import Organizer, Category, Championship
from apps.championship.models import ChampionshipCategory, ChampionshipInscription
from apps.championship.models import InscriptionLaps

class OrganizerForm(ModelForm):

    class Meta:
        model = Team


class CategoryForm(ModelForm):

    class Meta:
        model = Team


class ChampionshipForm(ModelForm):

    class Meta:
        model = Team

        fields = {
            'discipline', 'name', 'description', 'place', 'organizer',
            'start_date', 'finish_date', 'create_date', 'modified_date'
        }


class ChampionshipCategoryForm(ModelForm):

    class Meta:
        model = Team

        fields = {
            'championship', 'categoty', 'number_laps'
        }


class ChampionshipInscriptionForm(ModelForm):

    class Meta:
        model = Team

        fields = {
            'championship', 'number', 'position', 'rider', 'motorobike',
            'team', 'total_time', 'dif_time'
        }


class InscriptionLapsForm(ModelForm):

    class Meta:
        model = Team

        fields = {
            'inscription', 'number_lap', 'time'
        }