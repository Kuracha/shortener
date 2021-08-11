from django.db import models
from django.utils.crypto import get_random_string
from solo.models import SingletonModel


class CustomSettings(SingletonModel):
    short_url_length = models.PositiveIntegerField('Length of shortened url')

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return 'Settings'


class ShortenedUrl(models.Model):
    long_url = models.URLField('Url before shortening')
    short_url = models.URLField('Url after shortening', unique=True, blank=True)

    def create_shortened_url(self):
        length = CustomSettings.objects.first().short_url_length
        shortened_url = get_random_string(length)
        while ShortenedUrl.objects.filter(short_url=shortened_url).exists():
            shortened_url = get_random_string(length)
        return shortened_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.create_shortened_url()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Shortened Url'
        verbose_name_plural = 'Shortened Urls'

    def __str__(self):
        return str(self.short_url)
