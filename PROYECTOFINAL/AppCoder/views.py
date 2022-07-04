from django.shortcuts import render

from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Sede, Profesor
from AppCoder.forms import SedeFormulario, ProfesorFormulario, UserRegisterForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def sede (request):
      sede= Sede (nombre="Palermo", numero="1")
      sede.save()
      documentoDeTexto = f"--->Sede: {sede.nombre}   Numero: {sede.numero}"
      return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):
      return render(request, "AppCoder/inicio.html")

def socios(request):
      return render(request, "AppCoder/socios.html")

def clases(request):
      return render(request, "AppCoder/clases.html")

def sedes (request):
      if request.method == 'POST':
            miFormulario = SedeFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  sede= Sede (nombre=informacion['sede'], numero=informacion['numero']) 
                  sede.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario= SedeFormulario() 
      return render(request, "AppCoder/sedes.html", {"miFormulario":miFormulario})

def profesores(request):
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email']) 
                  profesor.save()
                  return render(request, "AppCoder/inicio.html") 
      else: 
            miFormulario= ProfesorFormulario() 
      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def buscar(request):
      if  request.GET["numero"]:
            numero = request.GET['numero'] 
            sedes= Sede.objects.filter(numero__icontains=numero)
            return render(request, "AppCoder/inicio.html", {"sedes":sedes, "numero":numero})
      else: 
        respuesta = "No enviaste datos"
      return HttpResponse(respuesta)
