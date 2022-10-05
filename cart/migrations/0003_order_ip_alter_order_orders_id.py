# Generated by Django 4.1.1 on 2022-09-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orders_id',
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]