"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from VetPlus import views

urlpatterns = [
    path('', views.inicioSesion,name='iniciarSesion'),
    path('portal.html',views.portal),
    path('index/',views.index),
    path('admin/', admin.site.urls),
    path('cliente/',views.cliente),
    path('administrador/',views.administrador),
    path('veterinario/', views.veterinario),
    path('tratamiento/',views.vet_tratamiento),
    path('recepcionista/',views.recepcionista),
    path('factura/',views.factura)

]
