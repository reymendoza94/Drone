from xml.dom import ValidationErr
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchController, Drone, Medication
from .forms import DroneForm, MedicationForm
# Create your views here.

@csrf_exempt
def create_drone(request):
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
        list_medication = data.get('medication', None).split(',')
        print(list_medication)
        if not Drone.objects.filter(id=data['drone']):
            return JsonResponse({"error":"Drone not found"}, status=404)
        else:            
            drone = Drone.objects.get(id=data['drone'])            
            if drone.state != 'loading' or drone.battery_capacity <=25:
                return JsonResponse({"error": "This dron don't be can loaded"})
            else:
                dispatch=DispatchController.objects.create(id=drone)
                # dispatch.save()

        if  list_medication: 
            for id_medication in list_medication:
                if not Medication.objects.filter(id=id_medication):
                    return JsonResponse({"error":"Medication not found"}, status=404)
                else:
                    medication = Medication.objects.get(id=id_medication)
                    if medication.weight <= drone.weight_limit:
                        drone.weight_limit = drone.weight_limit - medication.weight
                        drone.save()
                        medication_add=DispatchController.medication.objects.create(id=id_medication)
                        medication_add.save()
                    else:
                        return JsonResponse({"error": "The weight of the medication exceeds the loading weight limit."})
        
        return JsonResponse({"succes":"Dispatch create"}, status=201)
            
def list_medication_drone(request):
    if request.method == 'POST':
        data = request.POST.copy()
        model = DispatchController

        print (model.objects.filter(drone__id=data))

def list_drone_available(request):
    model = Drone
    list_drone = model.objects.filter(model.battery_capacity >= 25, model.state=='idle')
    if not list_drone:
        return JsonResponse({"error": "Don't drone available"},status= 404)
    return JsonResponse({"drone": list_drone}, status=201)
            

def check_drone_battery(request):
    if request.method == 'POST':
        data = request.POST.copy()
        model = Drone

        if not model.objects.filter(id=data['drone']):
            return JsonResponse({"error": "Drone not found"}, status=404)
        
        level_battery = model.objects.get(id=data['drone'])
        return JsonResponse({"succes":"The battery is {}"},level_battery,status=201)

        

        
    
