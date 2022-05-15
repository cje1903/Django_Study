__ORM(Object Relational Mapping)__ 📖
=====================================

> * 객체와 관계형 데이터베이스의 데이터를 매핑(연결)해주는 것 (객체 - 관계 매핑) <br/>
> * 객체 지향 프로그래밍: `class` - 관계형 데이터베이스: `table` <br/>
> * 객체 모델과 관계형 모델간의 불일치을 ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동 생성 -> 불일치 해결 <br/>
> * 데이터를 서로 교류하는 시스템 간에 사용하는 언어가 다르거나 조금씩 데이터를 기술하는 방식이 다르기에 **시스템에 변경되더라도 이를 하나의 코드로 통합해서 사용할 수 있는 기술**이 필요했는데요.<br/>
> 이 개념을 기존의 Object의 개념과 연결해서 하나의 클래스가 하나의 실제 시스템 자료구조에 연결되도록 추상화를 해서 연결한 것입니다.<br/>

> ORM의 개념은 굳이 웹이 아닌 다른 시스템에 대해서도 사용가능한 개념이지만,<br/>
> 우리가 할 django에서의 ORM은 **데이터베이스의 스키마를 소스코드로 기술, 재사용**할 수 있도록 하는 것입니다.<br/>
> ORM을 사용하게 되면 sqlite로 데이터베이스를 사용하다가 mysql로 데이터베이스를 변경할 때 코드는 거의 변경없이 사용할 수 있습니다. (물론, 데이터를 옮겨야 함)<br/>
> 
> 기본적으로 **하나의 모델 클래스에 하나의 테이블로 연동**이 됩니다.<br/>
> 그래서 우리가 웹 사이트에서 사용할 모든 **모델의 정보를 클래스로 기술하면, 여러 테이블의 메타 데이터를 포함하고 있는 데이터베이스 스키마를 기술한 것**이 됩니다.<br/>
--------------------------------------------

## `modles.py` 📖
```
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
> * 우선, `Restaurant` class 생성<br/>
> `python manage.py makemigrations, python manage.py migrate` 로 DB에 모델 적용<br/>
> `python manage.py shell` 터미널에서 장고 콘솔로 들어감<br/>
> `from third.models import Restaurant`로 `Restaurant`클래스를 불러온 후<br/>
> `Restaurant(name=’Deli Shop’, address=’Gangnam’).save()` 직접 레코드를 저장<br/>

> `Restaurant.objects.all()` 또는 `Restaurant.objects.all().values()`로 조회
> `Restaurant.objects.order_by('-created_at').values()` - 최신순으로 정렬
> `Restaurant.objects.get(pk=1).name` -> primary key가 1인 오브젝트의 name을 알 수 있습니다. **(pk는 자동 부여)**

더 자세한 건... 실제로 사용해보면서..하기...






