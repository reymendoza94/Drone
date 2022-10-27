from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Drone
from .forms import DroneForm
# Create your views here.

@csrf_exempt
def create_drone(request):
    data={}
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = DroneForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"succes":"creado"}, status=201)
        else:
            print(form.errors)
            return JsonResponse({"error":"no creado"}, status=400)

    
