from dataclasses import fields
from .models import Drone
from django import forms

class DroneForm(forms.ModelForm):
    
    class Meta:
        model = Drone
        fields = "__all__"
        
