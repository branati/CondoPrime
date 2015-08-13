# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0002_auto_20150813_1613'),
        ('morador', '0004_auto_20150812_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='apartamento',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='apartamento',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='unidade',
            field=models.ForeignKey(related_name='moradores', default=1, to='condominio.Unidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='tipo',
            field=models.CharField(default=1, max_length=2, choices=[(b'C', b'Carro'), (b'M', b'Moto')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='unidade',
            field=models.ForeignKey(related_name='veiculos', default=1, to='condominio.Unidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(verbose_name=b'data de nascimento', blank=True),
        ),
    ]
