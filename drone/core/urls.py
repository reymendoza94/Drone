from django.urls import path

from .views import create_drone, create_medication, create_dispatch_controler

urlpatterns = [
    path('create_drone/', create_drone, name="create_drone"),
    path('create_medication/', create_medication, name="create_medication"),
    path('create_dispatch_controler/', create_dispatch_controler, name="create_dispatch_controler"),
]
