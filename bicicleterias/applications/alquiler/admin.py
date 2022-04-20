from django.contrib import admin

from applications.alquiler.models import Alquiler


@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('nombre','hora_de_inicio','hora_de_fin','valor','fecha')
    list_editable = ('hora_de_inicio','hora_de_fin','valor','fecha')
    search_fields = ('nombre',)
    filter_horizontal = ('tipo_de_cicla',)

