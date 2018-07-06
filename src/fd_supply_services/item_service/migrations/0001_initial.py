# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('nsn', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='national stock number')),
                ('category', models.CharField(blank=True, default='', max_length=100)),
                ('common_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('aac', models.CharField(max_length=1, verbose_name='acquisition advice code')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('nsn',),
            },
        ),
        migrations.CreateModel(
            name='UnitOfIssue',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=16)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='ui',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item_service.UnitOfIssue'),
        ),
    ]