# Generated by Django 4.1.4 on 2023-01-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_services', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='preview',
            field=models.CharField(default=1, help_text='توضیحات مختصر در مورد این سرویس 60 حرف ', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='Description',
            field=models.TextField(help_text='توضیحات کامل در مورد این سرویس'),
        ),
        migrations.AlterField(
            model_name='service',
            name='svg_image',
            field=models.TextField(help_text='کد عکس (پرنکنید)'),
        ),
    ]