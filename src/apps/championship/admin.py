from django.contrib import admin
from apps.championship.models import (
        Organizer, Category, Championship,
        ChampionshipCategory, ChampionshipInscription,
        InscriptionLaps
    )


admin.site.register(Organizer)
admin.site.register(Category)
admin.site.register(Championship)
admin.site.register(ChampionshipCategory)
admin.site.register(ChampionshipInscription)
admin.site.register(InscriptionLaps)
