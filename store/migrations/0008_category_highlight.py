# Generated by Django 5.0.7 on 2024-07-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_stock_last_updated_alter_stock_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='highlight',
            field=models.BooleanField(default=False, verbose_name='Destacar'),
        ),
    ]
