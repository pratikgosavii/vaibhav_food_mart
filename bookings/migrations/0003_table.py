# Generated by Django 3.0.8 on 2022-05-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20220513_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField()),
                ('mobile_no', models.IntegerField()),
                ('persons', models.IntegerField(max_length=100)),
            ],
        ),
    ]
