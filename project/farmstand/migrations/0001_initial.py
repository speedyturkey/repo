# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('instructions', models.TextField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(default=b'na', max_length=5, choices=[(b'na', b'na'), (b'oz', b'Ounce'), (b'pt', b'Pint'), (b'qt', b'Quart'), (b'gl', b'Gallon'), (b'lb', b'Pound'), (b'bunch', b'Bunch'), (b'bu', b'Bushel')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('season', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('street_address1', models.CharField(max_length=64)),
                ('street_address2', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Week_Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(to='farmstand.Product')),
                ('week_id', models.ForeignKey(to='farmstand.Week')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='week',
            name='product',
            field=models.ManyToManyField(to='farmstand.Product', through='farmstand.Week_Product'),
        ),
        migrations.AddField(
            model_name='week',
            name='season_id',
            field=models.ForeignKey(to='farmstand.Season'),
        ),
        migrations.AddField(
            model_name='order',
            name='week_id',
            field=models.ForeignKey(to='farmstand.Week'),
        ),
    ]
