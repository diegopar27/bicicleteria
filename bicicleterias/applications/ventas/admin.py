from django.contrib import admin
from applications.ventas.models import Ventas


@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    filter_horizontal = ('marcos','zapatillas', 'tipo_de_cicla')
    list_filter = ('valor',)
    list_display = ('cliente','cantidad')
    list_editable = ('cantidad',)
    search_fields = ('cliente__nombre','cliente__apellido')