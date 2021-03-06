# Generated by Django 2.2.6 on 2019-11-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_auto_20191030_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='campus_country',
            field=models.CharField(help_text='Country Name of Campus', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='campus',
            name='contact_email',
            field=models.EmailField(help_text='Email of Campus', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='campus',
            name='contact_no',
            field=models.IntegerField(help_text='Contact Number of Campus', null=True),
        ),
    ]
