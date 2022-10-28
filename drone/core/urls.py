from django.urls import path

from .views import create_drone, create_medication

urlpatterns = [
    path('create_drone/', create_drone, name="create_drone"),
    path('create_medication/', create_medication, name="create_medication")
]
