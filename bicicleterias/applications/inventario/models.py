from django.db import models

# Create your models here.


class Marcos(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=50)
    garantia = models.IntegerField()
    descripcion= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Grupos (models.Model):
    marca = models.CharField(max_length=30)
    velocidades = models.CharField(max_length=40)
    garantia = models.CharField(max_length=50)

    def __str__(self):
        return self.marca

class Zapatillas(models.Model):
    marca=models.CharField(max_length=40)
    talla=models.CharField(max_length=2)
    estilo = models.CharField(max_length=40)


    def __str__(self):
        return self.marca





