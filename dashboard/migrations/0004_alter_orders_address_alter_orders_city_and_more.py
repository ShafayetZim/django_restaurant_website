# Generated by Django 4.0.2 on 2022-05-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
    ]