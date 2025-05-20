from django.shortcuts import render
from .forms import ClienteForm, ServicioForm, ContratacionForm, BusquedaClienteForm
from .models import Cliente

def inicio(request):
    return render(request, "blog/inicio.html")

def agregar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Cliente"})

def agregar_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Servicio"})

def agregar_contratacion(request):
    form = ContratacionForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Contratación"})

def buscar_cliente(request):
    resultado = None
    if request.GET.get("nombre"):
        form = BusquedaClienteForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            resultado = Cliente.objects.filter(nombre__icontains=nombre)
    else:
        form = BusquedaClienteForm()
    return render(request, "blog/busqueda.html", {"form": form, "resultado": resultado})
