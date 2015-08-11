from django.db import models

# Create your models here.


class Bloco(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Apartamento(models.Model):
    bloco = models.ForeignKey(Bloco)
    numero = models.IntegerField()

    def __unicode__(self):
        return self.bloco.nome + ' ' + self.numero