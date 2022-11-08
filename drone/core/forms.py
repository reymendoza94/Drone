from dataclasses import fields
from .models import Drone, Medication,DispatchController
from django import forms


# ---------------Drone Form-------------#
class DroneForm(forms.ModelForm):
    
    class Meta:
        model = Drone
        fields = "__all__"


# ---------------Medication Form-------------#
class MedicationForm(forms.ModelForm):
    
    class Meta:
        model = Medication
        fields = "__all__"
        

# ---------------Dispatch Controller Form-------------#
class DispatchControllerForm(forms.ModelForm):
    
    class Meta:
        model = DispatchController
        fields = "__all__"


       