__second__ 📖
===========
## __second 웹 앱의 디렉토리 구조__ 📖 <br/>
```
├─📁second
│  ├─🗀migrations
│  ├─🗀templates
│  │  └─🖿second
│  │    ├─base.html
│  │    ├─list.html
│  │    ├─create.html
│  │    └─confirm.html
│  ├─__init__.py
│  ├─admin.py
│  ├─apps.py
│  ├─forms.py
│  ├─models.py
│  ├─tests.py
│  ├─urls.py
│  └─views.py
```

## __URL Patterns__ 📖 <br/>
### 📃 `http://127.0.0.1:8000/second/list/`<br/>
<img src="" width="400px">

### 📃 `http://127.0.0.1:8000/second/create/`<br/>
<img src="" width="400px">

> `templates/select.html`의 form에서 input으로 받은 `number` 변수<br/>
> action(form으로 받은 데이터가 전달될 주소)은 'result'name을 갖는 url이고 'result'의 method가 GET.<br/>
> -> form의 input으로 받은 number을 GET방식의 'result'url로 전송하겠다.<br/>

### 📃 `http://127.0.0.1:8000/second/confirm/`<br/>
<img src="" width="400px">

> `http://127.0.0.1:8000/first/result/?number=7`<br/>
> 'result' url은 `?number=7` Query parameter로 데이터를 백엔드로 전달<br/>
> `views.py의 result함수`에서 `request.GET['number']`을 통해서 `number`을 받아옴<br/>
> `views.py의 result함수`에서 `templates/first/result.html`로 render할 때, `numbers`라는 이름의 변수로 함께 전달<br/>
> `templates/first/result.html`에서 `numbers`를 화면에 출력<br/>


## __그 외 설명__ 📖 <br/>
☑️ MTV 패턴 <br/>
> `Model`(models.py) 데이터 객체 정의& 데이터<br/>
> -> `View`(views.py) 데이터 가공 후 템플릿에 전달<br/>
> -> `Template`(templates/*.html) 사용자 화면에 출력<br/>

☑️ http 요청~응답 흐름 <br/>
> 클라이언트가 주소로 request을 보낸다<br/>
> 장고 웹 앱에 들어온 요청의 url을 확인<br/>
> 해당 url 담당 view로 전달<br/>
> view의 로직 실행 (필요시, model로 데이터 처리) 후 template로 전달<br/>
> template의 최종 html이 생성<br/>
> 클라이언트에게 response<br/>


