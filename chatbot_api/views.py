from django.shortcuts import render
from rest_framework.decorators import api_view
from .business import principal
from .serializers import PerguntaSerializer
from django.http.response import JsonResponse

# Create your views here.

@api_view(['GET'])
def obterPrincipal(request):
    perguntaPrincipal = principal.obterPerguntaPrincipal()
    perguntaPrincipal_serializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipal_serializer.data, safe=False)