# Generated by Django 5.0.7 on 2024-07-25 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created'], 'verbose_name': 'Orden', 'verbose_name_plural': 'Ordenes'},
        ),
    ]
