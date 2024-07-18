from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class SettingsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'settings.html'
