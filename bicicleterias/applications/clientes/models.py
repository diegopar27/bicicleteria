from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

