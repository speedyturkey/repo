# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmstand', '0010_auto_20151027_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week_Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(to='farmstand.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='week',
            name='product',
            field=models.ManyToManyField(to='farmstand.Product', through='farmstand.Week_Product'),
        ),
        migrations.AddField(
            model_name='week_product',
            name='week',
            field=models.ForeignKey(to='farmstand.Week'),
        ),
    ]
