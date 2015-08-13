# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='apartamento',
            name='bloco',
            field=models.ForeignKey(related_name='apartamentos', to='condominio.Bloco'),
        ),
    ]
