# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0006_auto_20151026_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='products',
            field=models.ManyToManyField(to='farmstand.Product'),
        ),
    ]
