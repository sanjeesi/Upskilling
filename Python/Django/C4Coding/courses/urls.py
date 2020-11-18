
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CoursesListView.as_view(), name="home"),
]
