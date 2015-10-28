# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(default=b'na', max_length=5, choices=[(b'na', b'na'), (b'oz', b'Ounce'), (b'pt', b'Pint'), (b'qt', b'Quart'), (b'gl', b'Gallon'), (b'lb', b'Pound'), (b'bunch', b'Bunch'), (b'bu', b'Bushel')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address1', models.CharField(max_length=64)),
                ('street_address2', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Week_Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(to='farmstand.Product')),
                ('week', models.ForeignKey(to='farmstand.Week')),
            ],
        ),
        migrations.AddField(
            model_name='week',
            name='product',
            field=models.ManyToManyField(to='farmstand.Product', through='farmstand.Week_Product'),
        ),
        migrations.AddField(
            model_name='week',
            name='season',
            field=models.ForeignKey(to='farmstand.Season'),
        ),
    ]
