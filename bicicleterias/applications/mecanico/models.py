from django.db import models

from applications.clientes.models import Clientes


class Mecanico(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=40)
    cedula = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


