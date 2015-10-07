# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('materia', models.CharField(max_length=50)),
                ('calificacion', models.IntegerField()),
                ('nombre', models.ForeignKey(to='principal.Alumno')),
            ],
        ),
        migrations.RemoveField(
            model_name='notas',
            name='nombre',
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
    ]
