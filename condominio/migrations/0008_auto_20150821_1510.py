# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0007_auto_20150821_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidade',
            options={'ordering': ['numero', 'bloco']},
        ),
    ]
