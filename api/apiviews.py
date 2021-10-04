from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .serializers import PersonaSerializer, TransformerSerializer
from .models import Transformer

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def test_auth(request):

    if request.user.is_authenticated:
        persona = Persona(nombre="Pablo", apellido="Fernandez")
    else:
        persona = Persona(nombre="NN", apellido="NN")
        
    serializer = PersonaSerializer(persona)

    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def transformer_list(request):
    """
    List all transformers, or create a new transformer
    """
    print('USER')
    print(request.user)
    if request.method == 'GET':
        transformer = Transformer.objects.all()
        serializer = TransformerSerializer(transformer, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransformerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    