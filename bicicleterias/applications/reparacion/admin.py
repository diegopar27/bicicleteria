from django.contrib import admin


from applications.reparacion.models import Reparacion


@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
       list_display = ('mecanico','cliente','tipo_de_cicla')
       list_editable = ('tipo_de_cicla',)
       search_fields = ('mecanico',)
