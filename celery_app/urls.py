"""Url for celery app."""
from django.urls import path
from .views import create_form, display_data

urlpatterns = [
    path('create/', create_form, name='create_form'),
    path('display/', display_data, name='display_data'),
]
