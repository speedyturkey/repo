# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street_address1',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street_address2',
            field=models.CharField(max_length=64),
        ),
    ]
