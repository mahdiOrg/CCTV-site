from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    types = (
        ('camera', 'camera'),
        ('alarm', 'alarm'),
        ('gps', 'gps'),
    )
    # auther =
    title = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=types, null=True)
    category = models.ManyToManyField(Category, related_name='products')
    preview = models.CharField(max_length=60, help_text='پیش نماش اطلاعات در کارت محصول')
    info = models.TextField(help_text='اطلاعات و توضیحات محصول')
    image = models.ImageField(upload_to='image/product')

    price = models.DecimalField(max_digits=9, decimal_places=0)
    add_time = models.DateField(auto_now_add=True)
    in_stock = models.BooleanField(default=True, help_text="در صورتی که محصول موجود نیست تیک برداشته شود")
    # slug = models.SlugField(null=True, blank=True, )
    sells = models.IntegerField()

    class Meta:
        ordering = ('-add_time',)

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     self.slug = slugify(self.title)
    #     super(Product, self, ).save()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=15)
    preview = models.CharField(max_length=60, help_text='توضیحات مختصر در مورد این سرویس 60 حرف ')
    image = models.ImageField(upload_to='image/service', blank=True, null=True)
    info = models.TextField(help_text="توضیحات کامل در مورد این سرویس")
    svg_image = models.TextField(help_text="کد عکس (پرنکنید)")

    def get_absolute_url(self):
        return reverse('products:service_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    add_time = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-add_time',)

    def __str__(self):
        return self.user , str(self.product) + self.text[:30]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return str(self.user) , str(self.product)
