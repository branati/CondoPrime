from django.contrib import admin
from .models import Condomino, Veiculo
# Register your models here.


class CondominoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'unidade')


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'unidade')
    

admin.site.register(Condomino, CondominoAdmin)
admin.site.register(Veiculo, VeiculoAdmin)