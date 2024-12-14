from django.db import models

# Create your models here.

class Usuario(models.Model):
    ROLES = [
        (1,'Administrativo'),
        (2,'Cliente'),
    ]
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    fono = models.CharField(max_length=20)
    rol = models.IntegerField(choices=ROLES,default=2)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre
