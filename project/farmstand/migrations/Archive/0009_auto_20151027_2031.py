# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0008_auto_20151027_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='week',
            old_name='products',
            new_name='something',
        ),
    ]
