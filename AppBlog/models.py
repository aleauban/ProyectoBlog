from ast import Delete
from typing import Any
from django.db import models

# Create your models here.

#Modelo de Post, posee todos los campos obligatorios:

class Post(models.Model):
    raza=models.CharField (max_length=30) 
    cualidad= models.CharField (max_length=30)
    descripcion= models.CharField (max_length=1000)
    autor= models.EmailField()
    fecha= models.DateField(auto_now_add=True)
    imagen= models.ImageField(upload_to='imagenblog')
    imagen1= models.ImageField(upload_to='imagenblog', null=True, blank=True)
    imagen2= models.ImageField(upload_to='imagenblog', null=True, blank=True)

# Nombre que se mostrara en panel administrador
    def __str__(self) -> str:   
        return self.raza