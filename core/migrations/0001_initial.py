# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.ImageField(upload_to='')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Images',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Publish data')),
                ('url_slug', models.CharField(max_length=150, verbose_name='URL Slug')),
                ('lang', models.PositiveSmallIntegerField(choices=[(1, 'Rus'), (2, 'Eng')], default=1, verbose_name='Language')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('is_page', models.BooleanField(default=False, verbose_name='Is single page')),
                ('head_image', models.ForeignKey(blank=True, db_column='head_image_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Image', verbose_name='Head image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
            },
        ),
    ]
