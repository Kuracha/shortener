from django import forms

from url_shortener.models import ShortenedUrl


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Provide here Url to shorten"}))

    class Meta:
        model = ShortenedUrl
        fields = ['long_url']
