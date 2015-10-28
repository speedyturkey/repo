# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0009_auto_20151027_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='week',
            old_name='something',
            new_name='product',
        ),
    ]
