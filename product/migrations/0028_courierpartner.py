# Generated by Django 3.1.2 on 2021-07-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_auto_20210729_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourierPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('track_no', models.CharField(max_length=250)),
            ],
        ),
    ]
