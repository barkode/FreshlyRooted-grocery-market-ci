# Generated by Django 4.2.16 on 2024-10-24 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_currency_productmessage_shippingday_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingDay',
            new_name='Shipping',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='shipping_day',
            new_name='shipping',
        ),
    ]
