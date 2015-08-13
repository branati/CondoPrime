# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, blank=True)),
                ('tipo', models.CharField(max_length=1, choices=[(b'V', b'Vertical'), (b'H', b'Horizontal')])),
                ('finalidade', models.CharField(max_length=1, choices=[(b'R', b'Residencial'), (b'C', b'Comercial'), (b'A', b'Ambos')])),
                ('telefone', models.CharField(max_length=15, blank=True)),
                ('cep', models.CharField(max_length=10, blank=True)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=50, blank=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.DecimalField(max_digits=4, decimal_places=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='apartamento',
            name='bloco',
        ),
    ]
