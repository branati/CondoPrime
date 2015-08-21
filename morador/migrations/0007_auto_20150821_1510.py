# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0006_auto_20150813_2148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condomino',
            options={'ordering': ['unidade']},
        ),
    ]
