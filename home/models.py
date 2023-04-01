from django.db import models


# Create your models here.

class AboutUS(models.Model):
    title = models.CharField(max_length=500, help_text=' پر رنگ خط اول با اندازه بزرگ')
    line2 = models.CharField(max_length=700, help_text='متن کم رنگ تر ')
    line3 = models.TextField(help_text='کم رنگ ترین متن با اندازه کوچکتر(متن اصلی ) ')


class Footer(models.Model):
    phone_number = models.IntegerField(max_length=11)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=700, null=True, blank=True, help_text='میتواند خالی هم باشد ')
    instagram_username= models.CharField(max_length=200, help_text='آدرس دقیق پیج اینستاگرام')
    whatsapp_number = models.IntegerField(help_text='شماره دقیق واتساپ همراه 98 بدون صفر و + ! ')
    telegram_id = models.CharField(max_length=200, help_text='دقیق تلگرام ID ')
    eitaa_id = models.CharField(max_length=200, help_text='ایتا ID ')

    class Meta:
        verbose_name_plural = 'Fotter'