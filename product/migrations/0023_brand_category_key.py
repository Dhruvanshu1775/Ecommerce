# Generated by Django 3.1.2 on 2021-07-23 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_productdetail_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='category_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
            preserve_default=False,
        ),
    ]
