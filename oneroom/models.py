from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    # 작성자
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 작성자 IP
    author_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)
    # 작성일자
    create_date = models.DateTimeField()
    # 수정일자
    modify_date = models.DateTimeField(blank=True, null=True)
    # 원룸이름
    title = models.TextField(blank=True, null=True)
    # LNG/LPG
    gas_type = models.TextField(blank=True, null=True)
    # 건물주 연락처
    owner_contact = models.TextField(blank=True, null=True)
    # 관리비
    manage_amount = models.IntegerField(blank=True, null=True)
    # 보증금
    deposit = models.IntegerField(blank=True, null=True)
    # 전월세 여부
    rent_type = models.TextField(blank=True, null=True)
    # 전월세 가격
    rent_amount = models.IntegerField(blank=True, null=True)
    # 전용 면적
    dedicated_area = models.FloatField(blank=True, null=True)
    # 공용 면적
    common_area = models.FloatField(blank=True, null=True)
    # 주차가능여부
    parking = models.IntegerField(blank=True, null=True)
    # 엘레베이터 여부
    elevator = models.IntegerField(blank=True, null=True)
    # 입주가능일
    moving_date = models.DateField(blank=True, null=True)
    # 방개수
    room_num = models.IntegerField(blank=True, null=True)
    # 방향
    direction = models.TextField(blank=True, null=True)
    # 화장실 개수
    toilet_num = models.IntegerField(blank=True, null=True)
    # 준공날짜
    construction_date = models.DateTimeField(blank=True, null=True)
    # 전체 층
    floor_total = models.IntegerField(blank=True, null=True)
    # 매물 층
    floor_num = models.IntegerField(blank=True, null=True)
    # 위도
    latitude = models.FloatField(blank=True, null=True)
    # 경도
    longitude = models.FloatField(blank=True, null=True)
    # 주소
    address = models.TextField(blank=True, null=True)

    browse_status = models.BooleanField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "매물 이름"


class Attribution(models.Model):
    post = models.TextField()
    A = models.IntegerField(blank=True, null=True)
    B = models.IntegerField(blank=True, null=True)
    C = models.IntegerField(blank=True, null=True)
    D = models.IntegerField(blank=True, null=True)
    E = models.IntegerField(blank=True, null=True)


class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="file_set")
    file = models.FileField(upload_to='oneroom/post')
    create_date = models.DateField()
    modify_date = models.DateField(blank=True, null=True)
