from django.urls import path
from . import views

urlpatterns = [
     path('principal', views.obterPrincipal, name='menu-principal')
]