# -*- encoding: utf8 -*-
from django.db import models
import morador

# Create your models here.


class Condominio(models.Model):
    COND_TIPO = (
        ('V', 'Vertical'),
        ('H', 'Horizontal'),
    )
    COND_FINALIDADE = (
        ('R', 'Residencial'),
        ('C', 'Comercial'),
        ('A', 'Ambos')
    )
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True)
    tipo = models.CharField(max_length=1, choices=COND_TIPO)
    finalidade = models.CharField(max_length=1, choices=COND_FINALIDADE)
    telefone = models.CharField(max_length=15, blank=True)

    cep = models.CharField(max_length=10, blank=True)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __unicode__(self):
        return self.nome



class Bloco(models.Model):
    condominio = models.ForeignKey(Condominio, related_name='blocos')
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome


class Unidade(models.Model):
    bloco = models.ForeignKey(Bloco, related_name='unidades')
    numero = models.DecimalField(max_digits=4, decimal_places=0)
    proprietario = models.ForeignKey('morador.Condomino', related_name='unidades', null=True, blank=True)




    def __unicode__(self):
        return u'%(numero)s - %(bloco)s' % {'bloco': self.bloco.nome,
                                           'numero': self.numero}