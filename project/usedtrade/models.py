from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usedtrade_post_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    title = models.TextField()
    content = models.TextField()
    price = models.IntegerField()
    delete_status = models.BooleanField()


class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usedtrade_file_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='file_set')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='usedtrade/post')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usedtrade_comment_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    delete_status = models.BooleanField()


class Nested(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usedtrade_nested_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='nested_set')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    delete_status = models.BooleanField()
