from django.urls import path, re_path

from . import views
# 현재 위치니깐 .

urlpatterns=[
    path('', views.index, name='index'),
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),

    # re_path(r'^select/(?P<year>[0-9]{4}/$'),
    #path('select/<int:year>/',views.select,..),
# select/2019/ 뭐 이런 url을 쓸 수 있게 됨 -> 2019를 year라는 변수에 정의, path에서 꺼내서 view.py의 select 메소드에서 받을 수 있음
]
# abc.com/restaurant/1923/reviews
# abc.com의 resaturant 중 1923번째 레스토랑의 리뷰 목록을 보고 싶어
# 이 때 1923을 path parameter이라고 함
# get과 post 방식

# GET -> abc.com/restaurant?id=1921
# -> query parameter

# abc.com/restaurant
# url에는 안보임, httprequest id=1923이라고 포함 (웹 브라우저에는 안보임) phone parameter?ㅋㅋㅋㅋ
