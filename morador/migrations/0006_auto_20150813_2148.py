# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morador', '0005_auto_20150813_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='Condomino',
        ),
    ]
