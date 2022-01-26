from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)
    # 만약 default 속성을 지정하지 않으면, 기존에 있던 값들에는 password 값이 안 들어 있음
    # 기존 것들의 password 속성은 Null,
    # 원래 어떠한 속성을 정의할 때, null을 지정해주지 않으면 기본적으로 null이면 안되고 무조건 채워져야 함
    # 1번 한식당 강남 [ ]
    # 2번 일식당 강북 [ ]
    image = models.CharField(max_length=500, default=None, null=True)
    # 이미지의 url을 넣을 거이기 때문에 문자여(string)으로 설정 - CharField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # 한개의 레스토랑 - 여러개의 리뷰 Many to One
    # 여러개인 리뷰에서 레스토랑 선언
    # Restaurant의 pk값을 가져옴 (pk=3번 레스토랑에 대한 리뷰입니다~)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)