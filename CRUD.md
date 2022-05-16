__CRUD (Create Read Update Delete)__ 📖
=======================================

> * __“CRUD는 대부분의 컴퓨터 소프트웨어가 갖는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)를
묶어서 일컫는 말이다. 사용자 인터페이스가 갖추어야 할 기능(정보의 참조/검색/갱신)을 가리키는 용어로서도 사용된다.”__
>
> * 식당 정보를 등록, 수정, 삭제하는 화면과 인터페이스를 구현해봅시다!!
----------------------------------------


## READ 📖
🍙 레스토랑 목록 화면 구현해보기 <br/>

**레스토랑 조회(READ) 플로우** : <br/>
➡️ `third/list/` url에서 views.list로 옴 -> GET방식 <br/>
➡️ 이때, 필요한 변수인 page를 전달하는 방법은 **`Query String`** <br/> 
ex) `도메인/third/list/?page=2` <br/>

```
//third/views.py

def list(request):
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review'))\
        .annotate(average_point=Avg('review__point'))   # __을 붙여주는 것이 장고 규칙
    # reviews_count 이름으로 Count('review')값을 넣게 됨
    # aggregation 연산, ('review')는 연산 대상
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page') ## third/list?page=1  queryparameter page=1
    items = paginator.get_page(page)    ## 현재 페이지에 맞는 레스토랑 오브젝트만 가져옴
    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)

```

> Restaurant 모델의 object들 외에도 해당 Restaurant를 참조하고 있는 Review의 개수, 그 리뷰들의 평점을 보여줄 것이다. <br/>
> `annotate`는 주석을 달다는 뜻으로, QuerySet의 각 객체에 추가될 주석이라고 생각하면 된다. *(장고에서는 필드를 추가해주겠다고 생각하면 된다)* <br/>
> --> Restaurant의 각 객체의 'Review'를 Count한 값과 'Review'의 'point'들의 Avg를 함께 주겠다는 뜻이다. <br/>
> <br/>
> Paginator은 위에서 Restaurant의 객체들에 annotate로 필드를 추가한 objects들을 __현재 페이지에 맞는 objects만을__ 넘겨주기 위해 사용<br/>
> 여기에선 5개의 객체를 한 페이지에 보여준다.<br/>
> <br/>
> *__third/list.html에 보내줄 데이터를 담은 변수들__* <br/>
> * Restaurant 모델 + reviews_count, average_point 필드 --> __`restaurants`__ <br/>
> * `restaurants`을 5개씩 나눈 Paginator --> __`paginator`__ <br/>
> * (('도메인/third/list')로 온) 'list'라는 name을 갖는 url에 GET방식으로 Request가 옴 -- `page` 정보를 가지고 옴<br/>
> * paginator가 page번째에 보여주는 restaurants --> __`items`__ <br/>
> * 'restaurants'라는 이름의 변수에 `items`를 담아서 __context 객체__ 를 `third/list.html`로 전달하면 끝.<br/>

<br/><br/>
🍙 레스토랑 상세 화면 구현해보기 <br/>

**레스토랑 상세하게 조회(READ) 플로우** : <br/>
➡️ 'third/list/'에서 자세히 보고 싶은 레스토랑의 '자세히 보기'버튼을 클릭<br/>
```
<a href="{% url 'restaurant-detail' id=item.id %}" class="card-link">자세히 보기</a>
```
➡️ 'restaurant-detail'라는 name의 url로 이동 - **GET 방식으로 접근** <br/>
➡️ 이 때, 필요한 변수인 id를 전달하는 방법은 **`Path Parameter`** <br/>
ex) `도메인/third/restaurant/7 <br/>

➡️ **`Path Parameter`** 로 받으면, 매개변수로 id를 받을 수 있게 됨 <br/>
```
def detail(request, id):
    if 'id' is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')
```
> 만약 해당 id를 가진 객체가 존재하지 않을 경우를 위해 `get_object_or_404` 사용<br/>
> 해당 id를 갖는 `Restaurant 객체`를 불러옴<br/>
> `해당 Restaurant를 참조하는 모든 Review 객체`를 불러옴 -- `Review.objects.filter(restaurant=item).all()`<br/>
> Restaurant, Review객체를 'third/detail.html'로 전달<br/>
> <br/>
> 만약 id가 None임 -> 'third/list/'로 돌아감 <br/>


----------------------------------------


## CREATE 📖
🍙 레스토랑 등록 구현해보기 <br/>

**레스토랑 등록 플로우** : <br/>
➡️ `상단 바에 있는 '등록' 을 클릭 (third/base.html)`  <br/>
➡️ `/third/create/ url로 이동` - **GET 방식으로 접근** <br/>
➡️ `create view`에서 사용자에게 레스토랑 정보를 입력받을 **`빈 Form`** 을 생성하고, `third/create.html`로 보내준다. <br/>
➡️ `third/create.html`에서 `Form을 입력`받고, 그 정보를 'restaurant-create'라는 name의 url로 보낸다. 이 때, **POST 방식으로 접근** <br/>
```
<form action="{% url 'restaurant-create' %}" method='post'>
```

➡️ `create view`에서 받아 온 Form이 유효한지 체크하고 DB에 저장해준다. <br/>
➡️ 'third/list' 화면을 response 해줘서 돌아간다. <br/>


우선, 사용자에게 레스토랑 정보를 입력받을 **ModelForm**을 만듭니다.
```
//third/forms.py
class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호')
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'image': _('이미지의 url을 입력해주세요.'),
            'password': _('게시물 비밀번호를 입력해주세요.')
        }
        widgets = {
            'password': forms.PasswordInput()   # 비밀번호 입력할 때 가려지게
        }
        error_messages = {
            'name': {
                'max_length': _('이름이 너무 깁니다. 30자 이하로 해주세요.')
            },
            'image': {
                'max_length': _('이미지의 주소의 길이가 너무 깁니다. 500자 이하로 해주세요.')
            },
            'password': {
                'max_length': _('비밀번호가 너무 깁니다. 20자 이하로 해주세요.')
            }
        }

```

> `Restaurant` 모델을 만들 때, 사용자가 입력해야하는 필드는 name, address, image, password 이렇게 4가지 입니다. <br/>
> 그것들에 대해 입력할 수 있게 모델 폼을 만들어줍니다. <br/>

**view 메서드**를 만들겠습니다. <br/>
`GET`
```
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})

```
> 상단 바의 등록 버튼을 통해 접근 가능 <br/>
> 빈 폼을 만들고 'third/create.html'로 함께 보낸다. <br/>


`POST`
```
// third/views.py
def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST) #POST요청으로 들어온 모든 데이터를 자동으로 레스토랑폼(모델폼)에 담아서 데이터 저장
        if form.is_valid():
            new_item = form.save()  # DB에 저장
        return HttpResponseRedirect('/third/list/')
```
> 'third/create.html'로 보내진 폼에 정보를 입력 받고, POST 방식으로 돌아옴 <br/>
> POST객체에 받아온 폼을 `form.save()`로 DB에 저장 <br/>
> 다시 '/third/list/'로 돌아감 <br/>

----------------------------------------

## UPDATE 📖
🍙 레스토랑 수정 구현해보기 <br/>

**레스토랑 수정 플로우** : <br/>
➡️ 'third/list/'에서 수정하고 싶은 레스토랑의 '수정하기'버튼을 클릭<br/>
```
// third/list.html
<a href="{% url 'restaurant-update' %}?id={{ item.id }}" class="card-link">수정하기</a>
```
➡️ `third/update/' url에서 views.update로 옴 -> **GET방식으로 접근** <br/>
➡️ 이때, 필요한 변수인 id를 전달하는 방법은 **`Query String`** <br/> 
ex) `도메인/third/update/?id=3` <br/> 
<br/> 
```
//third/views.py
    elif request.method == "GET":
        # item = Restaurant.objects.get(pk=request.GET.get('id')) ## third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
```
> 만약 해당 id를 가진 객체가 존재하지 않을 경우를 위해 `get_object_or_404` 사용<br/>
> 해당 id의 Restaurant 객체를 입력받을 때 사용했던 (create할 때) 폼인 RestaurantForm을 다시 받아 옴<br/>
> 'third/update.html'에 수정하기 위해 폼을 다시 내려보냄<br/>

<br/>
➡️ create할 때의 폼을 입력받듯이 update할 때의 폼을 입력받음 (수정사항이 바뀜) <br/>
```
// third/update.html
  <form action="{% url 'restaurant-update' %}" method='post'>
```

➡️ 'restaurant-update'라는 name을 갖는 url로 `POST`방식으로 접근<br/>
```
//third/views.py
    if request.method == "POST" and 'id' in request.POST:   ## 만약 id값이 실제 DB에 있는 값이 아님? -> list화면으로 돌아가!
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        # 만약 password 값이 POST request 를 통해 왔으면 'password'값이 왓을거고
        # 아니라면 디폴트로 ''빈 string
        form = UpdateRestaurantForm(request.POST, instance=item)  ## instance를 지정해주지 않으면 create와 똑같이 레스토랑의 새 오브젝트로 추가
        if form.is_valid() and password == item.password:
            item = form.save()
```
> **접근 방식이 `POST`이고, (?id=7)query string 방식으로 전달되는 'id'가 실제 DB에 존재하는 경우.**
> 만약 해당 id를 가진 객체가 존재하지 않을 경우를 위해 `get_object_or_404` 사용<br/>
> 해당 id를 갖는 Restaurant object를 item에 받아 옴
>
> POST 객체로 받아온 password가 존재하면 그대로 사용, 없을 경우 빈 string ''이 기본 <br/>
> 받아온 item 객체를 수정한 폼(POST로 받아온..)으로 수정 --> `UpdateRestaurantForm` <br/>
> 폼이 유효하고, password가 기존의 password와 동일한 경우 해당 오브젝트를 폼대로 DB에 저장 <br/>
> 만약 `UpdateRestaurantForm`에서 instance를 특별히 지정해주지 않는 경우 새 객체를 생성하는 것과 같음 -- CREATE <br/>
<br/>

➡️ 만약 `POST로 받아온 id`가 유효하지 않을 경우, 'third/list'페이지로 돌아가!!!
```
    return HttpResponseRedirect('/third/list')
```
<br/><br/>
➡️ 수정할 때 사용되는 폼
```
//third/forsm.py
class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']

```
> 'password' 제외하고, POST로 받아온 RestaurantForm을 받아와서 저장

----------------------------------------

## DELETE 📖
🍙 레스토랑 삭제 구현해보기 <br/>

**레스토랑 삭제 플로우** : <br/>
➡️ 상세화면인 'third/detail.html'의 '삭제하기' 버튼 클릭
```
<a href="{% url 'restaurant-delete' id=item.id %}">
```
➡️ 'restaurant-delete'라는 name을 갖는 url에 **GET방식으로 접근** && 이 때, **Path Parameter** 방식으로 어떤 레스토랑인지 `id` 전달 <br/>
ex) `도메인/third/restaurant/7/delete/`<br/>
```
// third/views.py
def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == "POST" and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('restaurant-detail', id=id)
    return render(request, 'third/delete.html', {'item': item})
```
> **Path Parameter** 방식으로 받은 view 메서드에서 id는 매개변수로 사용 가능 <br/>
> `POST` 객체에 받아온 `password`가 해당 id를 갖는 Restaurant의 기존 password와 일치하는지 확인 <br/>
> 일치한다면 `item.delete`를 통해 Restaurant object 삭제 <br/>
> 일치하지 않는다면, 'third/delete.html'로 돌아감. <br/>
