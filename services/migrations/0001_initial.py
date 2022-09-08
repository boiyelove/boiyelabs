# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Catalog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('timestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Timestamp')),
                ('name', models.CharField(max_length=15)),
                ('addr', models.URLField()),
                ('customer', models.CharField(max_length=12)),
                ('doc', models.FileField(upload_to='services/portfolio')),
            ],
            bases=('services.timestamp',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('timestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Timestamp')),
                ('name', models.CharField(max_length=35)),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.Catalog')),
            ],
            bases=('services.timestamp',),
        ),
        migrations.AddField(
            model_name='tag',
            name='services',
            field=models.ManyToManyField(to='services.Service'),
        ),
    ]
