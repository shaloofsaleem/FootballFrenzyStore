# Generated by Django 4.1.1 on 2022-09-26 07:12

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from=['product_name', 'sku'], unique=True),
        ),
    ]
