# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0004_unidade_proprietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espaco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('lotacao', models.PositiveSmallIntegerField()),
                ('regras', models.TextField()),
                ('tem_controle_chave', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='unidade',
            name='numero',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('espaco', models.OneToOneField(primary_key=True, serialize=False, to='condominio.Espaco')),
            ],
        ),
    ]
