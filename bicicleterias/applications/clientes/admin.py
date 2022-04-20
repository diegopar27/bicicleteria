from django.contrib import admin
from applications.clientes.models import Clientes


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula', 'telefono', 'direccion']
    list_editable = ['telefono', 'direccion']
    search_fields = ['nombre','apellido']
    list_filter = ['cedula']