# Generated by Django 4.2.16 on 2024-11-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, default='noimage.png', null=True, upload_to=''),
        ),
    ]