# Generated by Django 4.1.4 on 2023-01-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_services', '0009_alter_product_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]