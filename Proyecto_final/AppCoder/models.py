from django.db import models

# Create your models here.

class Sede (models.Model):
    nombre=models.CharField(max_length=30)
    numero = models.IntegerField()

    def __str__(self):
        return f"Sede: {self.nombre} - Numero: {self.numero}"

class Socio (models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    nacimiento=models.DateField()
    email= models.EmailField()
    numeroDeSocio= models.IntegerField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
  
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"

class Clase (models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeClase = models.DateField()  