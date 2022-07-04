from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Sede, Profesor, Avatar
from AppCoder.forms import SedeFormulario, ProfesorFormulario, UserRegisterForm, UserEditForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

import string
import random

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

def leerProfesores(request):
      profesores = Profesor.objects.all() 
      contexto= {"profesores":profesores} 
      return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      profesores = Profesor.objects.all() 
      contexto= {"profesores":profesores} 
      return render(request, "AppCoder/leerProfesores.html",contexto)

def editarProfesor(request, profesor_nombre):
      profesor = Profesor.objects.get(nombre=profesor_nombre)
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:  
                  informacion = miFormulario.cleaned_data
                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.save()
                  return render(request, "AppCoder/inicio.html") 
      else: 
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email}) 
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})

class SedeList(ListView):
      model = Sede 
      template_name = "AppCoder/sedes_list.html"

class SedeDetalle(DetailView):
      model = Sede
      template_name = "AppCoder/sedes_detalle.html"

class SedeCreacion(CreateView):
      model = Sede
      success_url = "/AppCoder/sede/list"
      fields = ['nombre', 'numero']

class SedeUpdate(UpdateView):
      model = Sede
      success_url = "/AppCoder/sede/list"
      fields  = ['nombre', 'numero']

class SedeDelete(DeleteView):
      model = Sede
      success_url = "/AppCoder/sede/list"

def logout_request(request):
      logout(request)
      messages.info(request, "Saliste sin problemas")
      return redirect("inicio")
     
def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  user = authenticate(username=usuario, password=contra)
                  if user is not None:
                        login(request, user)
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )
            else:
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})
      form = AuthenticationForm()
      return render(request,"AppCoder/login.html", {'form':form} )

def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            form = UserRegisterForm()     
      return render(request,"AppCoder/registro.html" ,  {"form":form})