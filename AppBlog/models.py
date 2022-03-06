from django.db import models

# Create your models here.

class Blog (models.Model):
    titulo=models.CharField (max_length=30) 
    subtitulo= models.CharField (max_length=30)
    cuerpo= models.CharField (max_length=1000)
    autor= models.EmailField()
    fecha= models.DateField(null=True)
    imagen= models.ImageField(upload_to='imagenblog')

    def __str__(self) -> str:
        return self.titulo