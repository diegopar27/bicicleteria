from django.db import models
from applications.tipos.models import Tipos_de_bicicletas



class Alquiler(models.Model):
    nombre = models.CharField(max_length=40)
    tipo_de_cicla = models.ManyToManyField(Tipos_de_bicicletas)
    hora_de_inicio = models.DateTimeField()
    hora_de_fin = models.DateTimeField()
    valor = models.CharField(max_length=30)
    fecha=models.DateTimeField()
    devuelto = models.BooleanField()

    def __str__(self):
        return self.nombre