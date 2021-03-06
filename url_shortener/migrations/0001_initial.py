# Generated by Django 3.0.8 on 2021-08-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url_length', models.PositiveIntegerField(default=8, verbose_name='Length of shortened url')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(verbose_name='Url before shortening')),
                ('short_url', models.URLField(blank=True, unique=True, verbose_name='Url after shortening')),
            ],
            options={
                'verbose_name': 'Shortened Url',
                'verbose_name_plural': 'Shortened Urls',
            },
        ),
    ]
