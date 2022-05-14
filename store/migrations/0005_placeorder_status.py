# Generated by Django 3.0.8 on 2022-05-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_placeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('recived', 'Recived'), ('accepted', 'Accepted'), ('preparing', 'Preparing'), ('out for delievry', 'Out for delievry'), ('accepted', 'Deliverd'), ('cancled', 'Cancled')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
