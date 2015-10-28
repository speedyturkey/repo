# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(default=b'na', max_length=5, choices=[(b'na', b'na'), (b'oz', b'Ounce'), (b'pt', b'Pint'), (b'qt', b'Quart'), (b'gl', b'Gallon'), (b'lb', b'Pound'), (b'bunch', b'Bunch'), (b'bu', b'Bushel')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
