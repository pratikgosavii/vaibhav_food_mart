# Generated by Django 3.0.8 on 2022-05-16 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220516_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_discription',
        ),
    ]
