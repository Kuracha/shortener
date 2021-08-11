from django.contrib import admin

from url_shortener.models import ShortenedUrl, CustomSettings


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):

    fields = [
        'long_url',
        'short_url',
    ]


@admin.register(CustomSettings)
class CustomSettingsAdmin(admin.ModelAdmin):
    pass
