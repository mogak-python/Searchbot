from django.urls import path
from . import views

urlpatterns = [
    path('command/register', views.save_birth, name='save_birth'),
]
