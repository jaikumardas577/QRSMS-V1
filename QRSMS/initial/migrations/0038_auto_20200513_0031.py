# Generated by Django 2.2 on 2020-05-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0037_auto_20200415_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='fee_per_CR',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='average',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='maximum',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='minimum',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='standard_devition',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
