# Generated by Django 3.1.2 on 2021-07-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=25),
        ),
    ]
