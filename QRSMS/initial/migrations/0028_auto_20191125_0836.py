# Generated by Django 2.2.7 on 2019-11-25 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0006_auto_20191123_0907'),
        ('initial', '0027_auto_20191125_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField()),
                ('attendance_slot', models.CharField(blank=True, choices=[(1, '8:00 AM - 9:00'), (2, '9:00 AM- 10:00'), (3, '10:00 AM- 11:00 PM'), (4, '11:00 AM- 12:00 PM'), (5, '12:00 PM- 1:00 PM'), (6, '1:00 PM- 2:00 PM'), (7, '2:00 PM- 3:00 PM'), (8, '3:00 PM- 4:00 PM')], max_length=256, null=True)),
                ('attendance_time_start', models.TimeField(blank=True, null=True)),
                ('attendance_interval_allowed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('qr_change_interval', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('duration_hour', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('scsddc', models.CharField(blank=True, max_length=256, null=True)),
                ('section', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'unique_together': {('scsddc', 'class_date', 'attendance_slot', 'section')},
            },
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_date', models.DateField()),
                ('attendance_slot', models.CharField(blank=True, choices=[(1, '8:00 AM - 9:00'), (2, '9:00 AM- 10:00'), (3, '10:00 AM- 11:00 PM'), (4, '11:00 AM- 12:00 PM'), (5, '12:00 PM- 1:00 PM'), (6, '1:00 PM- 2:00 PM'), (7, '2:00 PM- 3:00 PM'), (8, '3:00 PM- 4:00 PM')], max_length=256, null=True)),
                ('state', models.CharField(choices=[('NR', 'Not Registered'), ('P', 'Present'), ('A', 'Absent'), ('L', 'Late'), ('LV', 'Leave')], default='NR', max_length=256)),
                ('attendance_marked_time', models.TimeField(blank=True, null=True)),
                ('duration_hour', models.SmallIntegerField(blank=True, default=1, null=True)),
                ('attendance_type', models.CharField(blank=True, choices=[('M', 'Manual'), ('QR', 'QR-Code')], max_length=256, null=True)),
                ('scsddc', models.CharField(blank=True, max_length=256, null=True)),
                ('section', models.CharField(blank=True, max_length=256, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student_portal.Student')),
            ],
            options={
                'unique_together': {('student', 'scsddc', 'class_date', 'attendance_slot', 'section')},
            },
        ),
        migrations.AlterField(
            model_name='attendancesheet',
            name='attendance',
            field=models.ManyToManyField(blank=True, to='initial.StudentAttendance'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]