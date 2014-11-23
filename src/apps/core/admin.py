from django.contrib import admin
from apps.core.models import Country, State, Citie


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CitieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Citie, CitieAdmin)
