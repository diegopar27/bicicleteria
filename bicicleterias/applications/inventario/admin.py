from django.contrib import admin


from applications.inventario.models import Marcos,Grupos,Zapatillas


@admin.register(Marcos)
class MarcosAdmin(admin.ModelAdmin):
    list_display = ('nombre','marca','garantia','descripcion')
    list_editable = ('garantia','descripcion')
    list_filter = ('marca',)
    search_fields = ('nombre','marca')

@admin.register(Grupos)
class GruposAdmin(admin.ModelAdmin):
    list_display = ('marca', 'velocidades','garantia')
    list_filter = ('marca',)
    search_fields = ('marca','velocidades')
    list_editable = ('garantia',)
@admin.register(Zapatillas)
class ZapatillasAdmin(admin.ModelAdmin):
    list_display = ('marca','talla','estilo')
    list_filter = ('marca',)
    list_editable = ('talla','estilo')
