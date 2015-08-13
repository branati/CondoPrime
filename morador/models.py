# -*- encoding: utf8 -*-
from django.db import models
from condominio.models import Apartamento
# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('data de nascimento')
    email = models.EmailField()
    foto = models.CharField(max_length=50, null=True, blank=True)
    documento = models.CharField(max_length=14)
    apartamento = models.ForeignKey(Apartamento, related_name='moradores')


    def __unicode__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField(null=True, blank=True)
    foto = models.CharField(max_length=50, null=True, blank=True)
    apartamento = models.ForeignKey(Apartamento, related_name='veiculos')

    def __unicode__(self):
        return u'%(marca)s %(modelo)s %(placa)s' % {'marca': self.marca,
                                                    'modelo': self.modelo,
                                                    'placa': self.placa}
