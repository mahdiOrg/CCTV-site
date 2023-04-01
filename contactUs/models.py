from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    text = models.TextField()
    checked = models.BooleanField(default=False)
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('checked',)

    def __str__(self):
        return self.title
