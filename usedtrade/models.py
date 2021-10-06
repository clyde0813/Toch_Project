from django.db import models


# Create your models here.
class Post(models.Model):
    create_date = models.DateField()
    modify_date = models.DateField(null=True, blank=True)
    title = models.TextField()
    content = models.TextField()
    price = models.IntegerField()


class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='file_set')
    create_date = models.DateField()
    modify_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='usedtrade/post')
