# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0007_week_products'),
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
        migrations.DeleteModel(
            name='Week_Product',
        ),
    ]
