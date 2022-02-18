from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from telemetria.models import Telemetria, TelemetriaSerializer

# Create your views here.

def get_object_serializer(id):
    model = Telemetria.objects.get(p_id=id)
    serializer = TelemetriaSerializer(model)
    return serializer.data

def dashboard(request):
    json = get_object_serializer(61662)
    return render(request, 'dashboard.html', context={'telemetria': json})

@csrf_exempt
def telemetria_data(request):
    objId = request.GET.get('objId')
    objId = int(objId)
    objId += 1
    data = get_object_serializer(objId)
    return JsonResponse(data=data)