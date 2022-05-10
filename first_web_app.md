__first__ 📖
===========
## __first 웹 앱의 디렉토리 구조__ 📖 <br/>
```
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
```

## __URL Patterns__ 📖 <br/>
### 📃 `http://127.0.0.1:8000/first/`<br/>
<img src="https://user-images.githubusercontent.com/86587287/167660444-a64214c0-2e82-4f09-9966-b8961fb2d616.gif" width="400px">

### 📃 `http://127.0.0.1:8000/first/select/`<br/>
<img src="https://user-images.githubusercontent.com/86587287/167660429-848c9a3f-cd3c-4991-aefb-1fbee099fc63.gif" width="400px">

> `templates/select.html`의 form에서 input으로 받은 `number` 변수<br/>
> action(form으로 받은 데이터가 전달될 주소)은 'result'name을 갖는 url이고 'result'의 method가 GET.<br/>
> -> form의 input으로 받은 number을 GET방식의 'result'url로 전송하겠다.<br/>

### 📃 `http://127.0.0.1:8000/first/result/`<br/>
<img src="https://user-images.githubusercontent.com/86587287/167660440-fcd073c6-f247-465a-aea7-28392e846bb5.gif" width="400px">

> `http://127.0.0.1:8000/first/result/?number=7`<br/>
> 'result' url은 `?number=7` Query parameter로 데이터를 백엔드로 전달<br/>
> `views.py의 result함수`에서 `request.GET['number']`을 통해서 `number`을 받아옴<br/>
> `views.py의 result함수`에서 `templates/first/result.html`로 render할 때, `numbers`라는 이름의 변수로 함께 전달<br/>
> `templates/first/result.html`에서 `numbers`를 화면에 출력<br/>


## __그 외 설명__ 📖 <br/>
☑️ [`templates/first/base.html`](https://github.com/cje1903/Django_Study/blob/master/first/templates/first/base.html)
> title과 css와 같은 공통적인 부분 -> `{% extends 'first/base.html' %}`를 통해 불러올 수 있다. <br/>

☑️ `html의 form 태그` <br/>
> 
```
<form action=”데이터가 전달될 주소(요청/이동할 주소)” method=”http 요청 방식">
  <input type=”text” name=”title”/>
  <button type=”submit”>입력</button>
</form>
```

☑️ `query parameter` vs `path parameter` <br/>
데이터를 전송하기 위해서 `GET` vs 데이터를 전송 받기 위해서 `POST`<br/>
> `query parameter` - 경로 뒤에 입력 데이터를 함께 제공하는 형식 (`/first/result/?number=7`)<br/>
> ? 이후 부분을 __query string__ 라고 함, &로 연결하여 여러 개의 데이터를 넘길 수도 있음<br/><br/>
> `path variable` - 경로를 변수로써 사용 (`/first/result/7/`)<br/>
> urls.py에서 `path('first/result/<int:number>', views.result)` 로 정의하면 사용 가능<br/>
