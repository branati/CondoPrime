# -*- encoding: utf8 -*-
from django.contrib import admin
from .models import Bloco, Apartamento
# Register your models here.

class ApartamentoInline(admin.TabularInline):
    model = Apartamento
    extra = 8


class BlocoAdmin(admin.ModelAdmin):
    fields = ['nome']
    inlines = [ApartamentoInline]

admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Apartamento)