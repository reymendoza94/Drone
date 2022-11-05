from dataclasses import fields
from .models import Drone, Medication
from django import forms


class DroneForm(forms.ModelForm):
    
    class Meta:
        model = Drone
        fields = "__all__"


class MedicationForm(forms.ModelForm):
    
    class Meta:
        model = Medication
        fields = "__all__"
        

# class DispatchControllerForm(forms.ModelForm):
    
#     class Meta:
#         model = DispatchController
#         fields = "__all__"

    # def save(self) -> None:
    #     print(self.data)
    #     ids = str(self.data['medication']).split(', ')
    #     for id_medication in ids:


    #         return super().save()

       