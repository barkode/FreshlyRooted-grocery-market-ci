# Generated by Django 4.2.16 on 2024-10-24 12:25

from django.db import migrations, models


def update_product_images(apps, schema_editor):
    product = apps.get_model('products', 'Product')  # Replace with your app name
    new_image_path = 'noimage.png'  # Update with your new image path

    # Update all products with the new image
    product.objects.all().update(image_url=new_image_path)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image_url'),
    ]

    operations = [
        migrations.RunPython(update_product_images),
        migrations.AddField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
