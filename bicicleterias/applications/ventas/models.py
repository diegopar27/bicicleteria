from django.db import models
from applications.clientes.models import Clientes
from applications.inventario.models import Marcos, Grupos, Zapatillas
from applications.tipos.models import Tipos_de_bicicletas


class Ventas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    marcos = models.ManyToManyField(Marcos)
    grupos = models.OneToOneField(Grupos, on_delete=models.CASCADE)
    zapatillas = models.ManyToManyField(Zapatillas)
    tipo_de_cicla = models.ManyToManyField(Tipos_de_bicicletas)
    cantidad = models.IntegerField()
    valor = models.CharField(max_length=30)

    def __str__(self):
        return self.cliente.nombre