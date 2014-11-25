from django.contrib import admin
from apps.motorbike.models import Motorbike

# Register your models here.

class MotorbikeAdmin(admin.ModelAdmin):
    list_display = ('rider', 'bike_model', 'bike_brand', 'championship')
    search_fields = ('rider', 'bike_model', 'bike_brand', 'championship')

admin.site.register(Motorbike, MotorbikeAdmin)