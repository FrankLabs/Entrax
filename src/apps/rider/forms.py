# -*- coding: utf-8 *-*
from django.forms import ModelForm, TextInput
from apps.rider.models import ProfileRider


class ProfileRiderForm(ModelForm):
    class Meta:
        model = ProfileRider

        fields = {
            'user', 'birthday', 'location', 'team'
        }

        widgets = {
            'birthday': TextInput(
                attrs={'class': 'input_text'}
            ),
        }