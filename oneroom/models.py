from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    # 작성자
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    # 연세 가격
    year_amount = models.IntegerField(blank=True, null=True)
    # 면적
    dedicated_area = models.IntegerField(blank=True, null=True)
    # 주차가능여부
    parking = models.IntegerField(blank=True, null=True)
    # 엘레베이터 여부
    elevator = models.IntegerField(blank=True, null=True)
    # 방개수
    room_num = models.IntegerField(blank=True, null=True)
    # 화장실 개수
    toilet_num = models.IntegerField(blank=True, null=True)
    # 준공날짜
    construction_date = models.DateField(blank=True, null=True)
    # 전체 층
    floor_total = models.IntegerField(blank=True, null=True)
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


class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="file_set")
    file = models.FileField(upload_to='oneroom/post')
    create_date = models.DateField()
    modify_date = models.DateField(blank=True, null=True)
    rep = models.BooleanField(blank=True, null=True)


class Post_Status(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="status_set")
    remain = models.IntegerField(blank=True, null=True)
    hashtag1 = models.TextField(blank=True, null=True)
    hashtag2 = models.TextField(blank=True, null=True)
    hashtag3 = models.TextField(blank=True, null=True)
    aircon = models.BooleanField(blank=True, null=True)
    washer = models.BooleanField(blank=True, null=True)
    refrigerator = models.BooleanField(blank=True, null=True)
    desk = models.BooleanField(blank=True, null=True)
    closet = models.BooleanField(blank=True, null=True)
    shoeCloset = models.BooleanField(blank=True, null=True)
    induction = models.BooleanField(blank=True, null=True)
    doorLock = models.BooleanField(blank=True, null=True)
    videoPhone = models.BooleanField(blank=True, null=True)
    entrance = models.BooleanField(blank=True, null=True)
    CCTV = models.BooleanField(blank=True, null=True)
    fireAlarm = models.BooleanField(blank=True, null=True)
    gasAlarm = models.BooleanField(blank=True, null=True)
