from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Drone
# Create your views here.

@csrf_exempt
def create_drone(request):
    data={}
    
    if request.method == 'POST':
        data = request.POST.copy()
        serial_number = data.get('serial_number', '')
        model = data.get('model', '')
        weight_limit = data.get('weight_limit', '')
        battery_capacity = data.get('battery_capacity', '')
        state = data.get('state', '')
        Drone.objects.create(serial_number=serial_number, model=model, weight_limit=weight_limit, battery_capacity=battery_capacity, state=state)
       # print(data.get('weight_limit', ''))

    return JsonResponse(data)
