# Generated by Django 3.0.8 on 2022-05-16 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_book',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
            preserve_default=False,
        ),
    ]
