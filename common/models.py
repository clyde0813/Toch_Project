from django.contrib.auth.models import User
from django.db import models

from community.models import Post as CommunityPost
from usedtrade.models import Post as UsedTradePost


class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_receiver')
    create_date = models.DateTimeField()
    content = models.TextField()
    used_post = models.ForeignKey(UsedTradePost, on_delete=models.CASCADE, related_name='chat_post', blank=True,
                                  null=True)
    community_post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='community_post',
                                       blank=True, null=True)
