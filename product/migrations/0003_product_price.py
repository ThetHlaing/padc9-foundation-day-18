# Generated by Django 2.2.2 on 2020-01-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='0', max_length=255, verbose_name='Price of the product'),
        ),
    ]