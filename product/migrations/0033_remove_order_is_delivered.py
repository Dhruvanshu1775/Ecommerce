# Generated by Django 3.1.2 on 2021-07-29 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_auto_20210729_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_delivered',
        ),
    ]