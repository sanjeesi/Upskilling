from django.views.generic import ListView

from .models import CmdR

class HomePageView(ListView):
    model = CmdR
    template_name = 'home.html'