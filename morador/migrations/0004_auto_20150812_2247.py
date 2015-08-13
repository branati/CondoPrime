# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0001_initial'),
        ('morador', '0003_auto_20150812_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='apartamento',
            field=models.ForeignKey(related_name='moradores', default=1, to='condominio.Apartamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='apartamento',
            field=models.ForeignKey(related_name='veiculos', default=1, to='condominio.Apartamento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='foto',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
