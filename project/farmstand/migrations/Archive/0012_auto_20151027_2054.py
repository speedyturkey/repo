# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0011_auto_20151027_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week_product',
            name='product',
        ),
        migrations.RemoveField(
            model_name='week_product',
            name='week',
        ),
        migrations.RemoveField(
            model_name='week',
            name='product',
        ),
        migrations.DeleteModel(
            name='Week_Product',
        ),
    ]
