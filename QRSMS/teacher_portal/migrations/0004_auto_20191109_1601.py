# Generated by Django 2.2.6 on 2019-11-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_portal', '0003_auto_20191109_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='highest_qualification',
            field=models.SmallIntegerField(choices=[(1, 'Bachelors'), (2, 'Masters'), (3, 'Doctrate')], null=True),
        ),
    ]