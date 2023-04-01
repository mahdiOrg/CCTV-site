from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Service)
admin.site.register(models.Comment)
admin.site.register(models.Like)

