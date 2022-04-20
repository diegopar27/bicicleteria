from django.db import models


class Tipos_de_bicicletas(models.Model):
    nombre= models.CharField(max_length=40)
    marca=models.CharField(max_length=40)
    estilo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    garantia = models.IntegerField()

    def __str__(self):
        return self.nombre