# Generated by Django 2.2.6 on 2019-10-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0004_auto_20191018_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_year',
            field=models.SmallIntegerField(choices=[(1, 'FRESHMEN'), (2, 'SOPHOMORE'), (3, 'JUNIOR'), (4, 'SENIOR'), (5, 'VETERAN')], null=True),
        ),
        migrations.AlterField(
            model_name='regularcorecourseload',
            name='student_year',
            field=models.SmallIntegerField(choices=[(1, 'FRESHMEN'), (2, 'SOPHOMORE'), (3, 'JUNIOR'), (4, 'SENIOR'), (5, 'VETERAN')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='attending_semester',
            field=models.BooleanField(help_text='If the student is currently attending classes', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_semester',
            field=models.PositiveSmallIntegerField(help_text='Number of semester the student is Attending.', null=True),
        ),
    ]
