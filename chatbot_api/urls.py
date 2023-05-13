# from django.contrib import admin
# from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    # path('chatbot_api/', include('chatbot_api.urls')),
    # path('admin/', admin.site.urls),
    path('principal', views.obterPrincipal, name='menu-principal')
]