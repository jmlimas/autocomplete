# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151007_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='nombre',
            new_name='alumno',
        ),
    ]
