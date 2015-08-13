from django.contrib import admin
from .models import Pessoa, Veiculo
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'unidade')


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'unidade')
    

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Veiculo, VeiculoAdmin)