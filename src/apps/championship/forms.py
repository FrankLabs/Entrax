# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from django import forms

from apps.championship.models import ChampionshipInscription

class ChampionshipInscriptionForm(ModelForm):
    class Meta:
        model = ChampionshipInscription
        widgets = {
            'number': forms.NumberInput(attrs={'placeholder':'N°'}),
        }
