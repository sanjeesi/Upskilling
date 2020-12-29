from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

from . models import Courses

def login(request):
    return render(request, 'login.html')

class CoursesListView(ListView):
    model = Courses
    template_name = "home.html"