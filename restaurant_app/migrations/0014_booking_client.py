# Generated by Django 4.1.7 on 2023-04-13 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0013_place_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant_app.client'),
            preserve_default=False,
        ),
    ]
