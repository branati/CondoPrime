# -*- encoding: utf8 -*-
from django.db import models

# Create your models here.


class Bloco(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome


class Apartamento(models.Model):
    bloco = models.ForeignKey(Bloco, related_name='apartamentos')
    numero = models.IntegerField()
    #proprietario
    #responsavel


    def __unicode__(self):
        return u'%(numero)s %(bloco)s' % {'bloco': self.bloco.nome,
                                           'numero': self.numero}