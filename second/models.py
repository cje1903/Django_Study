from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()    # 문자열 길이 정의 x

    created_at = models.DateTimeField(auto_now_add=True)    # 자동으로 현재 시간 기록
    updated_at = models.DateTimeField(auto_now=True)    # 수정될 때마다 최근 수정시간 기록

    # num_stars = models.IntegerField() # 숫자

