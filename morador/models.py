# -*- encoding: utf8 -*-
from django.db import models
import condominio
# Create your models here.


class Condomino(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('data de nascimento', blank=True)
    email = models.EmailField()
    foto = models.CharField(max_length=50, null=True, blank=True)
    documento = models.CharField(max_length=14)
    unidade = models.ForeignKey('condominio.Unidade', related_name='moradores')


    def __unicode__(self):
        return self.nome


class Veiculo(models.Model):
    VEICULO_TIPO = (
        ('C', 'Carro'),
        ('M', 'Moto'),
    )
    tipo = models.CharField(max_length=2, choices=VEICULO_TIPO)
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField(null=True, blank=True)
    foto = models.CharField(max_length=50, null=True, blank=True)
    unidade = models.ForeignKey('condominio.Unidade', related_name='veiculos')

    def __unicode__(self):
        return u'%(marca)s %(modelo)s %(placa)s' % {'marca': self.marca,
                                                    'modelo': self.modelo,
                                                    'placa': self.placa}
