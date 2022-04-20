from django.db import models

from applications.clientes.models import Clientes
from applications.mecanico.models import Mecanico
from applications.tipos.models import Tipos_de_bicicletas

class Reparacion(models.Model):
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)
    tipo_de_cicla = models.OneToOneField(Tipos_de_bicicletas, on_delete=models.CASCADE)

    def __str__(self):
        return self.mecanico.nombre