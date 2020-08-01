from django.urls import path

from . import models
from .views import BirdsView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('birds', BirdsView.as_view()),
    path('version', models.version),
]