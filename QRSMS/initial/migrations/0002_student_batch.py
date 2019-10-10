# Generated by Django 2.2.5 on 2019-09-29 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.PositiveSmallIntegerField(default=2017, validators=[django.core.validators.RegexValidator('[0-9]{4}', message='Invalid Batch Year')], verbose_name='batch year'),
            preserve_default=False,
        ),
    ]