from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from url_shortener.forms import ShortenerForm
from url_shortener.models import ShortenedUrl


class ShortenerFormVIew(FormView):
    model = ShortenedUrl
    form_class = ShortenerForm
    template_name = 'shortener_form_view.html'
    template_name_success = 'generated_shortener.html'
    success_url = reverse_lazy('shortener')

    def get_template_names(self):
        if self.request.POST:
            return self.template_name_success
        else:
            return self.template_name

    def form_valid(self, form, **kwargs):
        domain = self.request.build_absolute_uri()
        new_url = form.save()
        short_url = domain + new_url.short_url
        context = self.get_context_data(**kwargs)
        context['short_url'] = short_url
        return self.render_to_response(context)


class ShortUrlRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        short_url = self.kwargs['short_url']
        try:
            long_url = ShortenedUrl.objects.get(short_url=short_url).long_url
        except ShortenedUrl.DoesNotExist:
            return reverse_lazy('wrong_url')
        return long_url
