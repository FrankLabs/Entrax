from django.forms import ModelForm
from apps.motorbike.models import Motorbike

class MotorbikeForm(ModelForm):

    class Meta:
        model = Motorbike