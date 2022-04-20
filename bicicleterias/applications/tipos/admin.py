from django.contrib import admin
from applications.tipos.models import Tipos_de_bicicletas
# Register your models here.


@admin.register(Tipos_de_bicicletas)
class Tipos_de_bicicletasAdmin (admin.ModelAdmin):
    list_display = ('nombre','marca','estilo','descripcion','garantia')
    list_editable = ('descripcion','garantia')
    search_fields = ('nombre','marca')

