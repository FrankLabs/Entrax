from django.contrib import admin
from apps.championship.models import Organization_Club, Championship
from apps.championship.models import Championship_Detail, Times, Level

# Register your models here.
class Organization_ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class Championship_DetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date')
    search_fields = ('name', 'place', 'club', 'club')

class TimesAdmin(admin.ModelAdmin):
    list_display = ('rider_level',)
    search_fields = ('rider_level',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('championship', 'rider', 'dicipline', 'category')
    search_fields = ('championship', 'rider')

admin.site.register(Organization_Club, Organization_ClubAdmin)
admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Championship_Detail, Championship_DetailAdmin)
admin.site.register(Times, TimesAdmin)
admin.site.register(Level, LevelAdmin)
