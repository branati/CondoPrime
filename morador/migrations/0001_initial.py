# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField(verbose_name=b'data de nascimento')),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=8)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('ano', models.IntegerField(max_length=4)),
                ('foto', models.CharField(max_length=50)),
            ],
        ),
    ]
