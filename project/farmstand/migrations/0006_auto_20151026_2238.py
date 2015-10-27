# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0005_auto_20151026_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='week',
            name='number',
            field=models.IntegerField(),
        ),
    ]
