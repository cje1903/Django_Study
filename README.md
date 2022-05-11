📚 __Django Study__ 📚
=========================
👩‍🏫 [`파이썬으로 장고(Django) 공략하기: 입문`](https://www.inflearn.com/course/django-course/) <br/>

## __프로젝트 디렉터리 구조__ 📖<br/>
Django는 하나의 프로젝트 내의 여러 개의 앱을 가집니다.<br/>
```
├─📁first_project
│  ├─__init__.py
│  ├─asgi.py
│  ├─settings.py
│  ├─urls.py
│  └─wsgi.py
│
├─📁first
│  ├─🗀migrations
│  ├─🗀static
│  │  └─🖿first
│  │    ├─image.png
│  │    └─style.css
│  ├─🗀templates
│  │  └─🖿first
│  │    ├─base.html
│  │    ├─index.html
│  │    ├─result.html
│  │    └─select.html
│  ├─__init__.py
│  ├─admin.py
│  ├─apps.py
│  ├─models.py
│  ├─tests.py
│  ├─urls.py
│  └─views.py
│
├─📁second
│  ├─🗀migrations
│  ├─🗀templates
│  │  └─🖿second
│  │    ├─confirm.html
│  │    ├─create.html
│  │    └─list.html
│  ├─__init__.py
│  ├─admin.py
│  ├─apps.py
│  ├─forms.py
│  ├─models.py
│  ├─tests.py
│  ├─urls.py
│  └─views.py
│
├─📁third
│  ├─🗀migrations
│  ├─🗀static
│  │  └─🖿third
│  │    └─style.css
│  ├─🗀templates
│  │  └─🖿third
│  │    ├─base.html
│  │    ├─create.html
│  │    ├─delete.html
│  │    ├─detail.html
│  │    ├─list.html
│  │    ├─review_create.html
│  │    ├─review_list.html
│  │    └─update.html
│  ├─__init__.py
│  ├─admin.py
│  ├─apps.py
│  ├─forms.py
│  ├─models.py
│  ├─tests.py
│  ├─urls.py
│  └─views.py
│
├─db.sqlite3
├─manage.py
├─requirements.txt
│
└─📁venv
```

## __Web Apps__ 📖<br/>
### [__first__](https://github.com/cje1903/Django_Study/blob/master/first_web_app.md) 📖<br/>
➡️ `http://127.0.0.1:8000/first/`<br/>
### [__second__](https://github.com/cje1903/Django_Study/blob/master/second_web_app.md) 📖<br/>
➡️ `http://127.0.0.1:8000/second/`<br/>
### [__third__](https://github.com/cje1903/Django_Study/blob/master/third_web_app) 📖<br/>
➡️ `http://127.0.0.1:8000/third/`<br/>
