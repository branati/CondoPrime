# -*- encoding: utf8 -*-
from django.contrib import admin
from .models import Bloco, Unidade, Condominio
# Register your models here.


class UnidadeInline(admin.TabularInline):
    model = Unidade
    extra = 8


class BlocoInLine(admin.TabularInline):
    model = Bloco
    extra = 2


class CondominioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Condomínio', {'fields': ['nome', 'cnpj', 'tipo', 'finalidade', 'telefone']}),
        ('Endereço', {'fields': ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']}),
    ]
    inlines = [BlocoInLine]


class BlocoAdmin(admin.ModelAdmin):
    fields = ['nome']
    inlines = [UnidadeInline]

admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Unidade)
admin.site.register(Condominio, CondominioAdmin)