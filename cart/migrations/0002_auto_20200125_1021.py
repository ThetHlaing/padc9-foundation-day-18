# Generated by Django 2.2.2 on 2020-01-25 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Customer ID',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='Product ID',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='QTY',
            new_name='qty',
        ),
    ]