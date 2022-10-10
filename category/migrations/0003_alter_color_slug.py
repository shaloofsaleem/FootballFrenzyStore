# Generated by Django 4.1 on 2022-10-08 04:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_brand_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, null=True, populate_from='title', unique_with=('color_code',)),
        ),
    ]
