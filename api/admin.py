from django.contrib import admin
from .models import Usuario
from .models import Inmueble
from .models import Arriendo
from .models import ServicioAdicional
from .models import Direccion
admin.site.register(Usuario)
admin.site.register(ServicioAdicional)
admin.site.register(Inmueble)
admin.site.register(Direccion)

class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'inmueble', 'fecha_inicio', 'fecha_fin', 'mostrar_total_a_pagar')

    def mostrar_total_a_pagar(self, obj):
        return obj.calcular_total_a_pagar()
    mostrar_total_a_pagar.short_description = 'Total a pagar'

admin.site.register(Arriendo, ArriendoAdmin)

