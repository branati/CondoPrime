from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('data de nascimento')
    email = models.EmailField()
    foto = models.CharField(max_length=50)
    documento = models.CharField(max_length=14)

    def __unicode__(self):
        return self.name


class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField(max_length=4)
    foto = models.CharField(max_length=50)

    def __unicode__(self):
        return self.marca + ' - ' + self.modelo + ' Placa: ' + self.placa
