from django.views.generic import ListView

# Create your views here.

from . models import Courses

class CoursesListView(ListView):
    model = Courses
    template_name = "home.html"