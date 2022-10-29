from copyreg import dispatch_table
from xml.dom import ValidationErr
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchController, Drone, Medication
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

        drone = None

        if Drone.objects.filter(id=data['drone']):
            drone = Drone.objects.get(id=data['drone'])

        else:
            return JsonResponse({"error":"Drone not found"}, status=404)

        if data['medication']:
            for m in data['medication']:
                if not Medication.objects.filter(id=int(m)).exists():
                    return JsonResponse({"error":"Medication {} not found".format(m)}, status=404)


        if DispatchController.objects.filter(drone__id=data['drone']):
            dispatch = DispatchController.objects.get(drone__id=data['drone'])
            
            if dispatch.drone.state != 'loading':
                return JsonResponse({"error":"Drone can be used reason: Status={}".format(dispatch.drone.get_state_display())}, status=400)
            else:
                if len(dispatch.medication.all()) != 0:
                    new_medication = Medication.objects.filter(id__in=data['medication'])
                    new_w = 0
                    for n in new_medication:
                        new_w += n.weight
                    if dispatch.drone.weight_limit < new_w:
                        return JsonResponse({"error":"Limit execed"}, status=400)
                    else:
                        if form.is_valid():
                            form.save()
                            return JsonResponse({"succes":"Dispatch create"}, status=201)

        else:
            if form.is_valid():
                form.save()
                return JsonResponse({"succes":"Dispatch create"}, status=201)
            else:
                return JsonResponse({"error": form.errors}, status=400)
            
def medication_loaded(request):
    if request.method == 'POST':
        data = request.POST.copy()
        model = DispatchController

        
    
