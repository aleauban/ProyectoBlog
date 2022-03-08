from ast import Delete
from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de Post, posee todos los campos obligatorios:
#Autor = Usuarios registrados. Si se elimina usuario se borran todos sus Post.

class Post(models.Model):
    raza=models.CharField (max_length=30) 
    cualidad= models.CharField (max_length=30)
    descripcion= models.TextField (max_length=800)
    autor= models.ForeignKey (User, on_delete=(models.CASCADE))
    fecha= models.DateField(auto_now_add=True)
    imagen= models.ImageField(upload_to='imagenblog')


# Nombre que se mostrara en panel administrador
    def __str__(self) -> str:   
        return self.raza