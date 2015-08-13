# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0002_auto_20150813_1613'),
        ('morador', '0005_auto_20150813_1613'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apartamento',
        ),
        migrations.AddField(
            model_name='unidade',
            name='bloco',
            field=models.ForeignKey(related_name='unidades', to='condominio.Bloco'),
        ),
        migrations.AddField(
            model_name='bloco',
            name='condominio',
            field=models.ForeignKey(related_name='blocos', default=1, to='condominio.Condominio'),
            preserve_default=False,
        ),
    ]
