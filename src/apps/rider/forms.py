# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django import forms

from apps.rider.models import ProfileRider

class NewRiderForm(ModelForm):
    class Meta:
        model = ProfileRider
        widgets = {
            'birthday': forms.DateInput(attrs={'placeholder':'aaaa-mm-dd'}),
        }
