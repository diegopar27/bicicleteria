from django.contrib import admin


from applications.mecanico.models import Mecanico


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_editable = ('cedula','telefono')
    list_display = ('nombre','apellidos','cedula','telefono')
    search_fields = ('nombre','apellido')
    list_filter = ('cedula',)
