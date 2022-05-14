__third__ 📖
===========
## __third 웹 앱의 디렉토리 구조__ 📖 <br/>
```
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
```

## __`models.py` & `forms.py`__ 📖 <br/>

### 📃 `models.py`<br/>
> `models.py`에 `Post` 라는 클래스(테이블) 생성 _(속성 - title, content, created_at, updated_at)_
```
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()    # 문자열 길이 정의 x

    created_at = models.DateTimeField(auto_now_add=True)    # 자동으로 현재 시간 기록
    updated_at = models.DateTimeField(auto_now=True)    # 수정될 때마다 최근 수정시간 기록
```
> database는 default로 `sqlite3`를 사용 <br/>
> `python manage.py makemigrations` => 변경 사항에 대한 마이그레이션 파일(0001_initial, 0002_alter_title_max_length 와 같이 변경 사항이 파일명에 표시 됨) 생성<br/>
> `python manage.py migrate` => 변경 사항을 데이터 베이스에 적용<br/>

<br/>

### 📃 `forms.py`<br/>
```
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용')
        }
        help_texts = {
            'title': _('제목을 입력해주세용(*￣3￣)╭'),
            'content': _('내용을 입력해주세용(*￣3￣)╭')
        }
        error_message = {
            'name': {
                'max_length': _("제목이 너무 깁니다. 30자 이하로 해주세요")
            }
        }

```
> __`Form`이 아닌 `ModelForm`을 사용하는 이유__ <br/>
> 모델 `Post`에 속성이 추가되면 `Form`도 그 때마다 수정해 주어야 하고<br/>
> form으로 받았던 데이터들을 다시 꺼내서 수정된 Post 모델 클래스의 인스턴스에 넣어주어야 하기 때문에 번거로움<br/>
> ❕ Django는 `Model form`으로 이 번거로움을 해결 ❕ <br/>


## __URL Patterns__ 📖 <br/>

### 📃 `http://127.0.0.1:8000/second/list/`<br/>
<img src="https://user-images.githubusercontent.com/86587287/167896152-53151854-6a19-44a2-a034-85c565dc2f69.png" width="400px">

```
//views.py
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)
```
> Post 클래스의 모든 오브젝트들 가져옴 -> `templates/second/list.html`로 데이터(context 형태)를 넘기겠다<br/>
> 오브젝트들의 `title`, `content` 속성을 화면에 출력<br/>
```
// templates/second/list.html
<a href="{% url 'create' %}" style="background-color:lightgray">입력하러 가기</a>
```
> a 태그를 누르면 `'create'라는 name의 url`로 이동하겠다 => `http://127.0.0.1:8000/second/create/`

<br/>

### 📃 `http://127.0.0.1:8000/second/create/`<br/>
1️⃣ `GET으로 'create'에 접근` <br/><br/>
<img src="https://user-images.githubusercontent.com/86587287/167896209-ebf180b8-6685-4a42-a205-29ec079ab2ee.png" width="400px">

```
// views.py
def create(request):
    # GET 으로 접속
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})
```
> * `http://127.0.0.1:8000/second/list/`에서 '입력하러 가기'를 클릭해서 접근 <br/>
> * url창에 `http://127.0.0.1:8000/second/create/`를 직접 쳐서 접근 <br/>
> 
> 데이터를 입력받기 위해 `PostForm`(ModelForm) __빈 객체__ 를 만들고 'form'이라는 이름으로 'second/create.html'로 전달 <br/>
> title과 content를 입력받을 수 있도록 `templates/second/create.html`를 render <br/>

```
// templates/second/create.html
<form action="{% url 'create' %}" method="post">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
  </table>
  <button type="submit">제출</button>
</form>
```

> 작성된 form의 데이터는 `'create'라는 name의 url` 로 전달될 것이다, http 요청 방식은 `POST`이다. <br/>
> _( first web app에서의 'templates/first/select/'에서 form태그로 전달한 데이터 number은 view로직으로 처리하고 끝나기 때문에(DB에 저장할 필요 X) forms.py가 필요 X )_<br/>

<br/>
2️⃣ `POST으로 'create'에 접근`<br/><br/>
<img src="https://user-images.githubusercontent.com/86587287/167907849-bc347f51-d0fc-4931-a6f4-d3c761daecbe.png" width="400px">

```
def create(request):
    # POST로 접속
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form)  # 레코드를 생성하는 코드 필요
            new_item = form.save()  # 이 구문 하나면, 모델 스키마에 저장
        return render(request, 'second/confirm.html', {'form': form})
```
> * `templates/second/create.html`의 form을 제출하면 `'create'라는 name의 url로 POST 방식`으로 데이터를 전달, 그 때 접근<br/>

```
//templates/second/create.html
<form action="{% url 'create' %}" method="post">
```
> `request` 객체에서 `PostForm`을 전달받는다<br/>
> 받은 PostForm이 유효한지 검사 후, 해당 레코드를 `Post 모델에 save`해준다.<br/>
> 받은 PostForm을 보여주는 `templates/second/confirm.html`을 render<br/>


## __그 외 설명__ 📖 <br/>
☑️ MTV 패턴 <br/>
> `Model`(models.py) 데이터 객체 정의& 데이터<br/>
> -> `View`(views.py) 데이터 가공 후 템플릿에 전달<br/>
> -> `Template`(templates/*.html) 사용자 화면에 출력<br/>

> `Model`: class Post 정의<br/>
> `View`: 데이터를 입력받고 로직처리 <br/>
> `Template`: View에서 넘겨준 데이터를 화면에 출력 <br/>


☑️ http 요청~응답 흐름 <br/>
> 1. 클라이언트가 주소로 `request`을 보낸다<br/>
> 2. 장고 웹 앱에 들어온 요청의 `url`을 확인<br/>
> 3. `urls.py`: 해당 url 담당 `view로 전달`<br/>
> 4. `view의 로직 실행` (필요시, model로 데이터 처리) 후 `template로 전달`<br/>
> 5. `template`: 최종 `html 생성`<br/>
> 6. 클라이언트에게 `response`<br/>
