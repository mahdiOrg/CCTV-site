# Generated by Django 4.1.4 on 2023-01-10 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_services', '0006_service_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title_in_English',
        ),
    ]
