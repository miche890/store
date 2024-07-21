from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
