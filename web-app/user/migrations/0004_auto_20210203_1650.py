# Generated by Django 3.1.5 on 2021-02-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210203_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='capa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='driver',
            name='isDriver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='driver',
            name='plateNum',
            field=models.CharField(default='None', max_length=999),
        ),
    ]
