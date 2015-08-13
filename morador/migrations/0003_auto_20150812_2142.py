# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0002_auto_20150812_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='foto',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
