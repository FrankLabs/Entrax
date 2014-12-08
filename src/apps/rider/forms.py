# -*- coding: utf-8 *-*
from django.forms import (
        ModelForm, TextInput, HiddenInput, ChoiceField, ValidationError, DateInput
    )
from django.forms.extras.widgets import SelectDateWidget

from apps.rider.models import ProfileRider, Team

from datetime import datetime as dt


class TeamForm(ModelForm):

    class Meta:
        model = Team


class ProfileRiderForm(ModelForm):

    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        try:
            print dt.date(dt.now())
            if (birthday > dt.date(dt.now())):
                raise ValidationError('La fecha de nacimiento no puede ser '
                        'en futuro.')
        except TypeError:
            pass
        return birthday

    class Meta:
        model = ProfileRider

        fields = {
            'user', 'birthday', 'team',
        }

        widgets = {
            'user': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre'}
            ),
            #'birthday': DateInput(
            #    attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}
            #),
            'birthday': SelectDateWidget(
                years=range(1950, int(dt.now().year)+1),
            ),
        }