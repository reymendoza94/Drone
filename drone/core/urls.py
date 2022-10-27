from django.urls import path

from .views import create_drone

urlpatterns = [
    path('create_drone/', create_drone, name="create_drone"),
]
