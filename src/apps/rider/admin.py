from django.contrib import admin
from apps.rider.models import ProfileRider, Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProfileRiderAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__first_name', 'user__last_name')
    list_filter = ('team',)


admin.site.register(Team, TeamAdmin)
admin.site.register(ProfileRider, ProfileRiderAdmin)
