# Generated by Django 4.1.4 on 2023-01-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_services', '0008_remove_product_slug_product_preview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.CharField(help_text='پیش نماش اطلاعات در کارت محصول', max_length=60),
        ),
    ]
