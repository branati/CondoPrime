from django.contrib import admin
from .models import Pessoa, Veiculo
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'apartamento')


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'apartamento')
    

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Veiculo, VeiculoAdmin)