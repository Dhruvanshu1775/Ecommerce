# Generated by Django 3.1.2 on 2021-07-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_remove_order_is_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackdetail',
            name='is_out_for_delivery',
            field=models.BooleanField(default=False),
        ),
    ]
