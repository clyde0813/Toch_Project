from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BoardName(models.Model):
    create_date = models.DateField()
    board_name = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_post_author')
    board = models.ForeignKey(BoardName, on_delete=models.CASCADE, related_name='post_set')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    title = models.TextField()
    content = models.TextField()
    delete_status = models.BooleanField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    delete_status = models.BooleanField()


class Nested(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_nested_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='nested_set')
    create_date = models.DateField()
    modify_date = models.DateField(null=True, blank=True)
    content = models.TextField()
    delete_status = models.BooleanField()


class Status(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_status_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    nested = models.ForeignKey(Nested, on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateField()
    view_status = models.BooleanField()
    like_status = models.BooleanField()
    dislike_status = models.BooleanField()
