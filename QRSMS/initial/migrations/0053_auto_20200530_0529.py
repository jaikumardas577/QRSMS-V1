# Generated by Django 2.2 on 2020-05-30 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0052_auto_20200530_0244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursesection',
            options={'ordering': ['-course']},
        ),
    ]
