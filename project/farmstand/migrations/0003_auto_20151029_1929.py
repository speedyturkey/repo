# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0002_auto_20151029_1728'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='week',
            unique_together=set([('season', 'number')]),
        ),
    ]
