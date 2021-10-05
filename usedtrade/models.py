from django.db import models


# Create your models here.
class usedtrade_post(models.Model):
    created_date = models.DateField()
    modified_date = models.DateField(null=True, blank=True)
    title = models.TextField()
    content = models.TextField()
    price = models.IntegerField()