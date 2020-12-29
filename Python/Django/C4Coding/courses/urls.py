
from django.urls import path

from . import views

urlpatterns = [
    path('viewCourses', views.CoursesListView.as_view(), name="home"),
]
