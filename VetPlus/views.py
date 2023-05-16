from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from VetPlus import models
from VetPlus.models import InicioSesion
from .forms import FormBusqueda_Cliente, FormInicioSesion
from requests import Session

# Create your views here.

def inicioSesion(request):
    form = FormInicioSesion()
    if request.method == 'POST':
        form = FormInicioSesion(request.POST)
        if form.is_valid():
            usuario_buscado = form.cleaned_data.get('usuario')
            contraseña_buscada = form.cleaned_data.get('contrasenia')
            request.session['datos']=[usuario_buscado, contraseña_buscada]
            print(usuario_buscado,contraseña_buscada)
            validacion = validarUsuario(request)
            if validacion:
                redireccion = validarUsuario(request)
                return redirect(redireccion)
            else:
                return render(request,'portal.html')
        else:
            print(form.errors)
            return render(request,'portal.html')
    else:
        return render(request,'portal.html')

arregloListaUsuarios =[ {'nombre':'veterinario','contraseña':'1234','tipo':'veterinario'},
                        {'nombre':'cliente','contraseña':'1234','tipo':'cliente'},
                        {'nombre':'admin','contraseña':'1234','tipo':'administrador'},
                        {'nombre':'recepcionista','contraseña':'1234','tipo':'recepcionista'}]

def validarUsuario(request):
    datos = request.session.get('datos')
    print("asd")
    for usuario in arregloListaUsuarios:
        if usuario['nombre'] == datos[0] and usuario['contraseña'] == datos[1]:
            if usuario['tipo'] == 'cliente':
                redireccion = '/cliente/'
            elif usuario['tipo']=='veterinario':
                    redireccion='/veterinario/'
            elif usuario['tipo']=='administrador':
                redireccion='/administrador/'
            elif usuario['tipo']=='recepcionista':
                redireccion='/recepcionista/'
            return redireccion
    return False


def resultadoBusqueda(request):
    form = FormBusqueda_Cliente()
    if request.method == 'POST':
        form = FormBusqueda_Cliente(request.POST)
        if form.is_valid():
            cliente_buscado = form.cleaned_data.get('cliente')
            rut_buscado = form.cleaned_data.get('rut')
            input_hidden = request.POST.get('origen_recepcion')
            request.session['datos'] = [cliente_buscado, rut_buscado]
            validacion = listaCliente(request)
            if validacion and input_hidden == "recepcion":
                redireccion = factura(request)
                return redirect(redireccion)
            else:
                return render(request, 'veterinario.html')
    else:
        return render(request, 'veterinario.html')

arregloListaCliente =[  {'nombre':'cliente1','rut':1234,'tipo':'cliente','mascota':'duque'},
                        {'nombre':'cliente2','rut':1234,'tipo':'cliente','mascota':'conde'},]


def listaCliente(request):
    datos = request.session.get('datos')
    for cliente in arregloListaCliente:
        print(cliente['rut'])
        if cliente['nombre'] == datos[0] and cliente['rut'] == datos[1]:
            if cliente['tipo'] == 'cliente':
                redireccion = '/tratamiento/'
            else:
                redireccion ='/veterinario/'
            return redireccion
    return False

def index(request):
    return render(request, 'index.html')

def cliente(request):
    return render(request,'cliente.html')

def administrador(request):
    return render(request, 'administracion.html')


def veterinario(request):
    resultadoBusqueda(request)
    return render(request, 'veterinario.html')

def portal (request):
    return render(request,'portal.html')

def vet_tratamiento(request):
    return render(request,'veterinario_tratamiento.html')

def recepcionista(request):
    return render(request,'recepcionista.html')

def factura(request):
    return render(request,'factura.html')