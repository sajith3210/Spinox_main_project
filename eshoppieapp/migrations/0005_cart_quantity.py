# Generated by Django 3.1.5 on 2021-04-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshoppieapp', '0004_auto_20210409_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]