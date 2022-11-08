from xml.dom import ValidationErr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchController, Drone, Medication
from .forms import DroneForm, MedicationForm, DispatchControllerForm
from django.core import serializers


# ---------------Create drone View-------------#
@csrf_exempt
def create_drone(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = DroneForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success":"Drone create"}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({"error":"Only POST method supported"})


# ---------------Create medication View-------------#
@csrf_exempt
def create_medication(request):    
    if request.method == 'POST':
        data = request.POST.copy()
        form = MedicationForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success":"Medication create"}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({"error":"Only POST method supported"})

        
# ---------------Create Dispatch Controller View-------------#
@csrf_exempt
def create_dispatch_controler(request):    
    if request.method == 'POST':
        data = request.POST.copy()

        if not Drone.objects.filter(id=data['drone']):
            return JsonResponse({"error":"Drone not found"}, status=404)  
        else:                      
            drone = Drone.objects.get(id=data['drone'])            
            if drone.state != 'loading' or drone.battery_capacity <=25:
                return JsonResponse({"error": "This dron don't be can loaded"})            

        if  data['medication']: 
            for id_medication in data['medication']:
                if not Medication.objects.filter(id=id_medication):
                    return JsonResponse({"error":"Medication not found"}, status=404)
                else:
                    medication = Medication.objects.get(id=id_medication)
                    if medication.weight > drone.weight_limit:
                        return JsonResponse({"error": "The weight of the medication exceeds the loading weight limit."})                                               
                    else:
                        drone.weight_limit = drone.weight_limit - medication.weight
                        drone.save()
                       
        form = DispatchControllerForm(data)
        if form.is_valid():
            form.save()               
            return JsonResponse({"success":"Dispatch create"}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        return JsonResponse({"error":"Only POST method supported"})


# ---------------List Medication by Drone View-------------#           
def list_medication_drone(request, id):
    if request.method == 'GET':
        dispatch = DispatchController.objects.filter(drone__id=id)

        if not dispatch:
            return JsonResponse({"error": "Dispatch not found"}, status= 404)
        else:
            list_medication = dispatch.medication
            print(list_medication)
            data = serializers.serialize("json", list_medication)
            return JsonResponse({"error": data}, status=201)
    else:
        return JsonResponse({"error":"Only GET method supported"})


# ---------------List Drones Availables View-------------#
def list_drone_available(request):    
    if request.method == 'GET':        
        list_drone = Drone.objects.filter(battery_capacity__gte=25, state='idle')

        if not list_drone:
            return JsonResponse({"error": "Don't drone available"}, status= 404)
        else:
            data = serializers.serialize("json", list_drone)        
            return JsonResponse({"drone": data}, status=201)

    else:
        return JsonResponse({"error":"Only GET method supported"})


# ---------------Chech Drone Battery View-------------#
def check_drone_battery(request, id):
    if request.method == 'GET':

        if not Drone.objects.filter(id=id):
            return JsonResponse({"error": "Drone not found"}, status=404)
        
        drone = Drone.objects.get(id=id)
        level_battery = drone.battery_capacity
        return JsonResponse({"success":"The battery is {}%".format(level_battery)},status=201)
    else:
        return JsonResponse({"error":"Only GET method supported"})
        

        
    
