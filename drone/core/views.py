from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Drone
from .forms import DispatchControllerForm, DroneForm, MedicationForm
# Create your views here.

@csrf_exempt
def create_drone(request):
    data={}
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = DroneForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"succes":"Drone create"}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        request.method == 'GET'
        return HttpResponse('Este es mi listado de drone')


@csrf_exempt
def create_medication(request):
    data={}
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = MedicationForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"succes":"Medication create"}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        request.method == 'GET'
        return HttpResponse('Este es mi listado de Medicamentos')


@csrf_exempt
def create_dispatch_controler(request):
    
    if request.method == 'POST':
        data = request.POST.copy()
        form = DispatchControllerForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"succes":"Dispatch create"}, status=201)
        else:
            return JsonResponse({"error": form.errors}, status=400)
        

    
