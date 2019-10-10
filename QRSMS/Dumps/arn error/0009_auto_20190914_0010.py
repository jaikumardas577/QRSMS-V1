# Generated by Django 2.2.5 on 2019-09-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0008_auto_20190912_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('uni_id', models.AutoField(primary_key=True, serialize=False, verbose_name='University Registration ID')),
                ('name', models.CharField(default='FAST NUCES', help_text='Name of Univeristy', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='ARN',
            field=models.PositiveIntegerField(default=1248, unique=True, verbose_name='Admission Registration Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNDEFINED'), ('O', 'OTHER')], default='UNDEFINED', max_length=50, verbose_name='Gender'),
        ),
        migrations.CreateModel(
            name='Campuses',
            fields=[
                ('campus_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Campus ID')),
                ('Address', models.CharField(help_text='Address of Campus', max_length=255)),
                ('campus_name', models.CharField(help_text='Name of Campus of University', max_length=255)),
                ('campus_city', models.CharField(help_text='City Name of Campus', max_length=255)),
                ('name', models.ForeignKey(default='0', help_text='A university can have many campuses', on_delete=django.db.models.deletion.SET_DEFAULT, to='initial.University', verbose_name='Universities Campus')),
            ],
        ),
    ]