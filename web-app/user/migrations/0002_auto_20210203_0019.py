# Generated by Django 3.1.5 on 2021-02-03 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driverinfo',
            name='capa',
        ),
        migrations.RemoveField(
            model_name='driverinfo',
            name='isDriver',
        ),
        migrations.RemoveField(
            model_name='driverinfo',
            name='plateNum',
        ),
    ]
