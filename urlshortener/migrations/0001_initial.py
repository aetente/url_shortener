# Generated by Django 3.2.8 on 2021-10-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('shortened_url', models.CharField(blank=True, max_length=15, unique=True)),
                ('hits', models.IntegerField(default=0)),
            ],
        ),
    ]
