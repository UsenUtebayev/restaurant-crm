# Generated by Django 4.1.7 on 2023-04-12 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0011_remove_drink_order_remove_food_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cook', to='restaurant_app.client'),
        ),
    ]
