# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0012_auto_20151027_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='product',
            field=models.ManyToManyField(to='farmstand.Product', through='farmstand.Week_Product'),
        ),
    ]
