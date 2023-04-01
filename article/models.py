from django.db import models
from product_services.models import Category
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to='image/article', null=True, blank=True)
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-add_time',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'id': self.id})


class Comment(models.Model):
    user = models.CharField(max_length=150)
    text = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-add_time',)

    def __str__(self):
        return self.user + str(self.article) + self.text[:30]
