# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0006_auto_20150821_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloco',
            options={'ordering': ['nome']},
        ),
    ]
