from xml.dom import ValidationErr
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
            return JsonResponse({'error': form.errors + "los valores"}, status=400)


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


@csrf_exempt
def create_dispatch_controler(request):
    
    if request.method == 'POST':
        data = request.POST.copy()       
        form = DispatchControllerForm(data)
        print(data)
        if not Drone.objects.filter(id=data['drone']):
            return JsonResponse({"error":"Drone not found"}, status=404)
        else:
            drone = Drone.objects.get(id=data['drone'])
            
            if drone.state != 'loading' or drone.battery_capacity <=25:
                return JsonResponse({"error": "This dron don't be can loaded"})

        if  data['medication']: 
            for id_medication in data['medication']:
                            
                if not Medication.objects.filter(id=id_medication):
                    return JsonResponse({"error":"Medication {} not found"}, id_medication, status=404)
                else:
                    medication = Medication.objects.get(id=id_medication)
                    if medication.weight <= drone.weight_limit:
                        drone.weight_limit = drone.weight_limit - medication.weight
                        drone.save()
                    else:
                        return JsonResponse({"error": "The weight of the medication exceeds the loading weight limit."})

        if form.is_valid():
            form.save()
            return JsonResponse({"succes":"Dispatch create"}, status=201)
        else:
            return JsonResponse({"error": form.errors}, status=400)
            
def medication_drone(request):
    if request.method == 'POST':
        data = request.POST.copy()
        model = DispatchController

        print (model.objects.filter(drone__id=data))
            




        
    
