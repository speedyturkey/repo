# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='week_id',
            new_name='week',
        ),
        migrations.RenameField(
            model_name='week',
            old_name='season_id',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='week_product',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='week_product',
            old_name='week_id',
            new_name='week',
        ),
    ]
