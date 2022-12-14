# Generated by Django 3.1.5 on 2021-02-04 22:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210203_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(default='None', max_length=999)),
                ('startTime', models.DateTimeField()),
                ('passengerNum', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])),
                ('driver_id', models.IntegerField(default='0')),
                ('owner_id', models.IntegerField(default='0')),
                ('confirmed', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='rideInfo',
        ),
        migrations.AlterField(
            model_name='driver',
            name='capa',
            field=models.IntegerField(choices=[(2, 2), (5, 5), (7, 7)], default=0),
        ),
        migrations.AlterField(
            model_name='driver',
            name='carType',
            field=models.CharField(choices=[('economy', 'economy'), ('business', 'business'), ('luxury', 'luxury'), ('presidential', 'presidential')], default='None', max_length=999),
        ),
    ]
