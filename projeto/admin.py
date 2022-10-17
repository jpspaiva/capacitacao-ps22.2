from django.contrib import admin
from .models import Formulario, Inicio
from .models import QuemSomos
from .models import Servicos
from .models import Portfolio
from .models import Contato
# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display1 = ('id', 'titulo')

admin.site.register(Inicio, InicioAdmin)
admin.site.register(QuemSomos)
admin.site.register(Servicos)
admin.site.register(Portfolio)
admin.site.register(Contato)
admin.site.register(Formulario)