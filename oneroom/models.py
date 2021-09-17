from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class oneroom_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    gas_type = models.TextField(blank=True, null=True)
