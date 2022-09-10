from django.contrib import admin
from django.utils.html import format_html

from .models import Team


# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'fisrt_name', 'last_name', 'designation', 'thumbnail', 'created_at')
    list_display_links = ('id', 'fisrt_name',)
    search_fields = ('fisrt_name', 'last_name', 'designation',)
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
