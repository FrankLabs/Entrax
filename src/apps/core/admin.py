from django.contrib import admin
from apps.core.models import Country, State, Citie


class Country_InLine(admin.TabularInline):
    model = State
    extra = 0


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [Country_InLine]


class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CitieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Citie, CitieAdmin)
