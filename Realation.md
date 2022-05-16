__Realation 📖__
=================
> * **Relation**은 모델과 모델 간의 종속 관계 <br/><br/>
> * **Many-to-Many** - ex) 출판사와 저작물의 관계 (하나의 출판사에서 여러 개의 저작물, 하나의 저작물을 여러 개의 출판사에서 OK)
> * **Many-to-One** - ex) 게시글과 댓글의 관계 (하나의 게시글에 여러 개의 댓글)
> * **One-to-One** - ex) 여권과 사람의 관계 (한 사람은 하나의 여권, 하나의 여권은 한 사람에게만.)
--------------------------
### **`Restaurant`** 모델과 **`Review`** 모델은 **Many-to-One** 관계!!
<img src="https://user-images.githubusercontent.com/86587287/168635497-5d0b36f8-fc49-4e9f-82f4-f27992211aeb.png" width="650px">

```
//third/models.py
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
```
> * `Review`에서 Restaurant를 ForeignKey로 참조할 때, `참조무결성`을 위해 `on_delete`옵션이 붙는다. <br/>
> `on_delete`는 ForeignKeyField가 바라보는 `Restaurant의 객체가 삭제될 때`, 처리 법 <br/>
>
> **`CASCADE`**: ForeignKeyField를 포함하는 Review 모델 인스턴스 몽땅 삭제 <br/>
> **`PROTECT`**: 해당 요소(restaurant field)가 같이 삭제되지 않도록 Protected Error을 발생시킨다. <br/>
> **`SET_NULL`**: ForeignKeyField(restaurant)값을 NULL로 바꾼다. (null=True일 때만 사용 가능) <br/>
> **`SET_DEFAULT`**: default 값으로 변경한다.
> **`SET`**: SET에 설정된 함수에 의해 설정
> **`DO_NOTHING`**: 아무것도 하지 않음. (참조 무결성을 해칠 수 있어서 잘 사용 X)


<br/>

* Restaurant 모델의 primary key인 id는 migration 과정에서 자동으로 생성되는 값임<br/>
* `id`는 models.py에서 정의해준 적 없는 field 이지만 생성되어있음
```
// migration/0002_review.py
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
```

