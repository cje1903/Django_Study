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

## __URL Patterns__ 📖<br/>
> `first` __web app__ <br/>
> > `http://127.0.0.1:8000/first/`<br/>
> > `http://127.0.0.1:8000/first/select/`<br/>
> > `http://127.0.0.1:8000/first/result/`<br/>

> `second` __web app__ <br/>
> > `http://127.0.0.1:8000/second/list/`<br/>
> > `http://127.0.0.1:8000/second/create/`<br/>
> > `http://127.0.0.1:8000/second/confirm/`<br/>

> `third` __web app__ <br/>
> > `http://127.0.0.1:8000/third/list/`<br/>
> > `http://127.0.0.1:8000/third/create/`<br/>
> > `http://127.0.0.1:8000/third/update/`<br/>
> > `http://127.0.0.1:8000/third/restaurant/<int:id>/`<br/>
> > `http://127.0.0.1:8000/third/restaurant/<int:id>/delete/`<br/>
> > `http://127.0.0.1:8000/third/restaurant/<int:restaurant_id>/review/create/`<br/>
> > `http://127.0.0.1:8000/third/restaurant/<int:restaurant_id>/review/delete/<int:review_id>/`<br/>
> > `http://127.0.0.1:8000/third/review/list/`<br/>

> `admin` __admin__ <br/>
