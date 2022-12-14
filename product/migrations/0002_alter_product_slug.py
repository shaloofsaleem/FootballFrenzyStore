# Generated by Django 4.1.1 on 2022-09-26 04:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='product_name', unique=True),
        ),
    ]
