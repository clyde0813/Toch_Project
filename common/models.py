from django.contrib.auth.models import User
from django.db import models

from community.models import Post as CommunityPost
from usedtrade.models import Post as UsedTradePost


class ChatRoom(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatroom_author')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatroom_receiver', null=True)


class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_author')
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_receiver')
    create_date = models.DateTimeField()
    content = models.TextField()
    used_post = models.ForeignKey(UsedTradePost, on_delete=models.CASCADE, related_name='usedtrade_post', blank=True,
                                  null=True)
    community_post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='community_post',
                                       blank=True, null=True)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, related_name='chat_list')
    # 챗 읽었는지 유뮤 0=안읽음, 1=읽음
    chat_status = models.BooleanField(default=0)
