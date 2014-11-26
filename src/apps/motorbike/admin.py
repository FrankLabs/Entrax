from django.contrib import admin
from apps.motorbike.models import Motorbike_Brand, Motorbike_Model, Motorbike

# Register your models here.
class Motorbike_BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class Motorbike_ModelAdmin(admin.ModelAdmin):
    list_display = ('bike_brand','name',)
    search_fields = ('bike_brand','name',)
    list_filter = ('bike_brand',)


class MotorbikeAdmin(admin.ModelAdmin):
    list_display = ('rider', 'bike_model',)
    search_fields = ('rider', 'bike_model',)


admin.site.register(Motorbike_Brand, Motorbike_BrandAdmin)
admin.site.register(Motorbike_Model, Motorbike_ModelAdmin)
admin.site.register(Motorbike, MotorbikeAdmin)