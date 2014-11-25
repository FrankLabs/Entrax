from django.contrib import admin
from apps.championship.models import Club, ChampionshipDetail, Statistic


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'discipline', 'club_organizer', 'location', 'date')
    search_fields = ('name',)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('category', 'championship', 'rider',
                    'result', 'laps', 'time')
    search_fields = ('category',)


admin.site.register(Club, ClubAdmin)
admin.site.register(ChampionshipDetail, ChampionshipAdmin)
admin.site.register(Statistic, StatisticAdmin)
