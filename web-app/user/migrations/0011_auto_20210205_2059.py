# Generated by Django 3.1.5 on 2021-02-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_ride_shareable'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='carType',
            field=models.CharField(default='None', max_length=999),
        ),
        migrations.AddField(
            model_name='ride',
            name='driverName',
            field=models.CharField(default='None', max_length=999),
        ),
        migrations.AddField(
            model_name='ride',
            name='plateNum',
            field=models.CharField(default='None', max_length=999),
        ),
    ]