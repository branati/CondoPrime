# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0006_auto_20150813_2148'),
        ('condominio', '0003_auto_20150813_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='proprietario',
            field=models.ForeignKey(related_name='unidades', blank=True, to='morador.Condomino', null=True),
        ),
    ]
