from atexit import register
from copyreg import dispatch_table
from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from .models import *

# Register your models here.

class MedicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    class Meta:
        model = Medication
        fields = "__all__"
        display_list = ['id', 'name']

admin.site.register(Drone)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(DispatchController)