from django.urls import path

from .views import (create_drone, 
create_medication, 
create_dispatch_controler, 
list_medication_drone, 
check_drone_battery,
list_drone_available)

urlpatterns = [
    path('create_drone/', create_drone, name="create_drone"),
    path('create_medication/', create_medication, name="create_medication"),
    path('create_dispatch_controler/', create_dispatch_controler, name="create_dispatch_controler"),
    path('list_medication_drone/<str:id>', list_medication_drone, name="list_medication_drone"),    
    path('list_drone_available/', list_drone_available, name="list_drone_available"),
    path('check_drone_battery/<str:id>', check_drone_battery, name="check_drone_battery"),
]
