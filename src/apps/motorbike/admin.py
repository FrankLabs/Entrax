from django.contrib import admin
from apps.motorbike.models import Motorbike


class MotorbikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'rider')
    search_fields = ('name',)


admin.site.register(Motorbike, MotorbikeAdmin)
