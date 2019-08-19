from django.urls import path
from django.contrib import admin
from . import views


app_name = 'roulettehome'

urlpatterns = [
    path('', views.home, name='home'),
]