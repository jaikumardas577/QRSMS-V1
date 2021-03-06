# Generated by Django 2.2.7 on 2019-11-23 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0023_auto_20191123_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancesheet',
            name='attendance',
            field=models.ManyToManyField(blank=True, to='initial.Attendance'),
        ),
        migrations.AlterField(
            model_name='attendancesheet',
            name='scsddc',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='attendancesheet',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_portal.Student'),
        ),
    ]
