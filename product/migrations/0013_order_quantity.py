# Generated by Django 3.1.2 on 2021-07-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_order_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]