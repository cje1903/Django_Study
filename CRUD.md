__CRUD (Create Read Update Delete)__ ๐
=======================================

> * __โCRUD๋ ๋๋ถ๋ถ์ ์ปดํจํฐ ์ํํธ์จ์ด๊ฐ ๊ฐ๋ ๊ธฐ๋ณธ์ ์ธ ๋ฐ์ดํฐ ์ฒ๋ฆฌ ๊ธฐ๋ฅ์ธ Create(์์ฑ), Read(์ฝ๊ธฐ), Update(๊ฐฑ์ ), Delete(์ญ์ )๋ฅผ
๋ฌถ์ด์ ์ผ์ปซ๋ ๋ง์ด๋ค. ์ฌ์ฉ์ ์ธํฐํ์ด์ค๊ฐ ๊ฐ์ถ์ด์ผ ํ  ๊ธฐ๋ฅ(์ ๋ณด์ ์ฐธ์กฐ/๊ฒ์/๊ฐฑ์ )์ ๊ฐ๋ฆฌํค๋ ์ฉ์ด๋ก์๋ ์ฌ์ฉ๋๋ค.โ__
>
> * ์๋น ์ ๋ณด๋ฅผ ๋ฑ๋ก, ์์ , ์ญ์ ํ๋ ํ๋ฉด๊ณผ ์ธํฐํ์ด์ค๋ฅผ ๊ตฌํํด๋ด์๋ค!!
----------------------------------------


## READ ๐
๐ ๋ ์คํ ๋ ๋ชฉ๋ก ํ๋ฉด ๊ตฌํํด๋ณด๊ธฐ <br/>

**๋ ์คํ ๋ ์กฐํ(READ) ํ๋ก์ฐ** : <br/>
โก๏ธ `third/list/` url์์ views.list๋ก ์ด -> GET๋ฐฉ์ <br/>
โก๏ธ ์ด๋, ํ์ํ ๋ณ์์ธ page๋ฅผ ์ ๋ฌํ๋ ๋ฐฉ๋ฒ์ **`Query String`** <br/> 
ex) `๋๋ฉ์ธ/third/list/?page=2` <br/>

```
//third/views.py

def list(request):
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review'))\
        .annotate(average_point=Avg('review__point'))   # __์ ๋ถ์ฌ์ฃผ๋ ๊ฒ์ด ์ฅ๊ณ  ๊ท์น
    # reviews_count ์ด๋ฆ์ผ๋ก Count('review')๊ฐ์ ๋ฃ๊ฒ ๋จ
    # aggregation ์ฐ์ฐ, ('review')๋ ์ฐ์ฐ ๋์
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page') ## third/list?page=1  queryparameter page=1
    items = paginator.get_page(page)    ## ํ์ฌ ํ์ด์ง์ ๋ง๋ ๋ ์คํ ๋ ์ค๋ธ์ ํธ๋ง ๊ฐ์ ธ์ด
    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)

```

> Restaurant ๋ชจ๋ธ์ object๋ค ์ธ์๋ ํด๋น Restaurant๋ฅผ ์ฐธ์กฐํ๊ณ  ์๋ Review์ ๊ฐ์, ๊ทธ ๋ฆฌ๋ทฐ๋ค์ ํ์ ์ ๋ณด์ฌ์ค ๊ฒ์ด๋ค. <br/>
> `annotate`๋ ์ฃผ์์ ๋ฌ๋ค๋ ๋ป์ผ๋ก, QuerySet์ ๊ฐ ๊ฐ์ฒด์ ์ถ๊ฐ๋  ์ฃผ์์ด๋ผ๊ณ  ์๊ฐํ๋ฉด ๋๋ค. *(์ฅ๊ณ ์์๋ ํ๋๋ฅผ ์ถ๊ฐํด์ฃผ๊ฒ ๋ค๊ณ  ์๊ฐํ๋ฉด ๋๋ค)* <br/>
> --> Restaurant์ ๊ฐ ๊ฐ์ฒด์ 'Review'๋ฅผ Countํ ๊ฐ๊ณผ 'Review'์ 'point'๋ค์ Avg๋ฅผ ํจ๊ป ์ฃผ๊ฒ ๋ค๋ ๋ป์ด๋ค. <br/>
> <br/>
> Paginator์ ์์์ Restaurant์ ๊ฐ์ฒด๋ค์ annotate๋ก ํ๋๋ฅผ ์ถ๊ฐํ objects๋ค์ __ํ์ฌ ํ์ด์ง์ ๋ง๋ objects๋ง์__ ๋๊ฒจ์ฃผ๊ธฐ ์ํด ์ฌ์ฉ<br/>
> ์ฌ๊ธฐ์์  5๊ฐ์ ๊ฐ์ฒด๋ฅผ ํ ํ์ด์ง์ ๋ณด์ฌ์ค๋ค.<br/>
> <br/>
> *__third/list.html์ ๋ณด๋ด์ค ๋ฐ์ดํฐ๋ฅผ ๋ด์ ๋ณ์๋ค__* <br/>
> * Restaurant ๋ชจ๋ธ + reviews_count, average_point ํ๋ --> __`restaurants`__ <br/>
> * `restaurants`์ 5๊ฐ์ฉ ๋๋ Paginator --> __`paginator`__ <br/>
> * (('๋๋ฉ์ธ/third/list')๋ก ์จ) 'list'๋ผ๋ name์ ๊ฐ๋ url์ GET๋ฐฉ์์ผ๋ก Request๊ฐ ์ด -- `page` ์ ๋ณด๋ฅผ ๊ฐ์ง๊ณ  ์ด<br/>
> * paginator๊ฐ page๋ฒ์งธ์ ๋ณด์ฌ์ฃผ๋ restaurants --> __`items`__ <br/>
> * 'restaurants'๋ผ๋ ์ด๋ฆ์ ๋ณ์์ `items`๋ฅผ ๋ด์์ __context ๊ฐ์ฒด__ ๋ฅผ `third/list.html`๋ก ์ ๋ฌํ๋ฉด ๋.<br/>

<br/><br/>
๐ ๋ ์คํ ๋ ์์ธ ํ๋ฉด ๊ตฌํํด๋ณด๊ธฐ <br/>

**๋ ์คํ ๋ ์์ธํ๊ฒ ์กฐํ(READ) ํ๋ก์ฐ** : <br/>
โก๏ธ 'third/list/'์์ ์์ธํ ๋ณด๊ณ  ์ถ์ ๋ ์คํ ๋์ '์์ธํ ๋ณด๊ธฐ'๋ฒํผ์ ํด๋ฆญ<br/>
```
<a href="{% url 'restaurant-detail' id=item.id %}" class="card-link">์์ธํ ๋ณด๊ธฐ</a>
```
โก๏ธ 'restaurant-detail'๋ผ๋ name์ url๋ก ์ด๋ - **GET ๋ฐฉ์์ผ๋ก ์ ๊ทผ** <br/>
โก๏ธ ์ด ๋, ํ์ํ ๋ณ์์ธ id๋ฅผ ์ ๋ฌํ๋ ๋ฐฉ๋ฒ์ **`Path Parameter`** <br/>
ex) `๋๋ฉ์ธ/third/restaurant/7 <br/>

โก๏ธ **`Path Parameter`** ๋ก ๋ฐ์ผ๋ฉด, ๋งค๊ฐ๋ณ์๋ก id๋ฅผ ๋ฐ์ ์ ์๊ฒ ๋จ <br/>
```
def detail(request, id):
    if 'id' is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')
```
> ๋ง์ฝ ํด๋น id๋ฅผ ๊ฐ์ง ๊ฐ์ฒด๊ฐ ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ๋ฅผ ์ํด `get_object_or_404` ์ฌ์ฉ<br/>
> ํด๋น id๋ฅผ ๊ฐ๋ `Restaurant ๊ฐ์ฒด`๋ฅผ ๋ถ๋ฌ์ด<br/>
> `ํด๋น Restaurant๋ฅผ ์ฐธ์กฐํ๋ ๋ชจ๋  Review ๊ฐ์ฒด`๋ฅผ ๋ถ๋ฌ์ด -- `Review.objects.filter(restaurant=item).all()`<br/>
> Restaurant, Review๊ฐ์ฒด๋ฅผ 'third/detail.html'๋ก ์ ๋ฌ<br/>
> <br/>
> ๋ง์ฝ id๊ฐ None์ -> 'third/list/'๋ก ๋์๊ฐ <br/>


----------------------------------------


## CREATE ๐
๐ ๋ ์คํ ๋ ๋ฑ๋ก ๊ตฌํํด๋ณด๊ธฐ <br/>

**๋ ์คํ ๋ ๋ฑ๋ก ํ๋ก์ฐ** : <br/>
โก๏ธ `์๋จ ๋ฐ์ ์๋ '๋ฑ๋ก' ์ ํด๋ฆญ (third/base.html)`  <br/>
โก๏ธ `/third/create/ url๋ก ์ด๋` - **GET ๋ฐฉ์์ผ๋ก ์ ๊ทผ** <br/>
โก๏ธ `create view`์์ ์ฌ์ฉ์์๊ฒ ๋ ์คํ ๋ ์ ๋ณด๋ฅผ ์๋ ฅ๋ฐ์ **`๋น Form`** ์ ์์ฑํ๊ณ , `third/create.html`๋ก ๋ณด๋ด์ค๋ค. <br/>
โก๏ธ `third/create.html`์์ `Form์ ์๋ ฅ`๋ฐ๊ณ , ๊ทธ ์ ๋ณด๋ฅผ 'restaurant-create'๋ผ๋ name์ url๋ก ๋ณด๋ธ๋ค. ์ด ๋, **POST ๋ฐฉ์์ผ๋ก ์ ๊ทผ** <br/>
```
<form action="{% url 'restaurant-create' %}" method='post'>
```

โก๏ธ `create view`์์ ๋ฐ์ ์จ Form์ด ์ ํจํ์ง ์ฒดํฌํ๊ณ  DB์ ์ ์ฅํด์ค๋ค. <br/>
โก๏ธ 'third/list' ํ๋ฉด์ response ํด์ค์ ๋์๊ฐ๋ค. <br/>


์ฐ์ , ์ฌ์ฉ์์๊ฒ ๋ ์คํ ๋ ์ ๋ณด๋ฅผ ์๋ ฅ๋ฐ์ **ModelForm**์ ๋ง๋ญ๋๋ค.
```
//third/forms.py
class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('์ด๋ฆ'),
            'address': _('์ฃผ์'),
            'image': _('์ด๋ฏธ์ง url'),
            'password': _('๊ฒ์๋ฌผ ๋น๋ฐ๋ฒํธ')
        }
        help_texts = {
            'name': _('์ด๋ฆ์ ์๋ ฅํด์ฃผ์ธ์.'),
            'address': _('์ฃผ์๋ฅผ ์๋ ฅํด์ฃผ์ธ์.'),
            'image': _('์ด๋ฏธ์ง์ url์ ์๋ ฅํด์ฃผ์ธ์.'),
            'password': _('๊ฒ์๋ฌผ ๋น๋ฐ๋ฒํธ๋ฅผ ์๋ ฅํด์ฃผ์ธ์.')
        }
        widgets = {
            'password': forms.PasswordInput()   # ๋น๋ฐ๋ฒํธ ์๋ ฅํ  ๋ ๊ฐ๋ ค์ง๊ฒ
        }
        error_messages = {
            'name': {
                'max_length': _('์ด๋ฆ์ด ๋๋ฌด ๊น๋๋ค. 30์ ์ดํ๋ก ํด์ฃผ์ธ์.')
            },
            'image': {
                'max_length': _('์ด๋ฏธ์ง์ ์ฃผ์์ ๊ธธ์ด๊ฐ ๋๋ฌด ๊น๋๋ค. 500์ ์ดํ๋ก ํด์ฃผ์ธ์.')
            },
            'password': {
                'max_length': _('๋น๋ฐ๋ฒํธ๊ฐ ๋๋ฌด ๊น๋๋ค. 20์ ์ดํ๋ก ํด์ฃผ์ธ์.')
            }
        }

```

> `Restaurant` ๋ชจ๋ธ์ ๋ง๋ค ๋, ์ฌ์ฉ์๊ฐ ์๋ ฅํด์ผํ๋ ํ๋๋ name, address, image, password ์ด๋ ๊ฒ 4๊ฐ์ง ์๋๋ค. <br/>
> ๊ทธ๊ฒ๋ค์ ๋ํด ์๋ ฅํ  ์ ์๊ฒ ๋ชจ๋ธ ํผ์ ๋ง๋ค์ด์ค๋๋ค. <br/>

**view ๋ฉ์๋**๋ฅผ ๋ง๋ค๊ฒ ์ต๋๋ค. <br/>
`GET`
```
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})

```
> ์๋จ ๋ฐ์ ๋ฑ๋ก ๋ฒํผ์ ํตํด ์ ๊ทผ ๊ฐ๋ฅ <br/>
> ๋น ํผ์ ๋ง๋ค๊ณ  'third/create.html'๋ก ํจ๊ป ๋ณด๋ธ๋ค. <br/>


`POST`
```
// third/views.py
def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST) #POST์์ฒญ์ผ๋ก ๋ค์ด์จ ๋ชจ๋  ๋ฐ์ดํฐ๋ฅผ ์๋์ผ๋ก ๋ ์คํ ๋ํผ(๋ชจ๋ธํผ)์ ๋ด์์ ๋ฐ์ดํฐ ์ ์ฅ
        if form.is_valid():
            new_item = form.save()  # DB์ ์ ์ฅ
        return HttpResponseRedirect('/third/list/')
```
> 'third/create.html'๋ก ๋ณด๋ด์ง ํผ์ ์ ๋ณด๋ฅผ ์๋ ฅ ๋ฐ๊ณ , POST ๋ฐฉ์์ผ๋ก ๋์์ด <br/>
> POST๊ฐ์ฒด์ ๋ฐ์์จ ํผ์ `form.save()`๋ก DB์ ์ ์ฅ <br/>
> ๋ค์ '/third/list/'๋ก ๋์๊ฐ <br/>

----------------------------------------

## UPDATE ๐
๐ ๋ ์คํ ๋ ์์  ๊ตฌํํด๋ณด๊ธฐ <br/>

**๋ ์คํ ๋ ์์  ํ๋ก์ฐ** : <br/>
โก๏ธ 'third/list/'์์ ์์ ํ๊ณ  ์ถ์ ๋ ์คํ ๋์ '์์ ํ๊ธฐ'๋ฒํผ์ ํด๋ฆญ<br/>
```
// third/list.html
<a href="{% url 'restaurant-update' %}?id={{ item.id }}" class="card-link">์์ ํ๊ธฐ</a>
```
โก๏ธ `third/update/' url์์ views.update๋ก ์ด -> **GET๋ฐฉ์์ผ๋ก ์ ๊ทผ** <br/>
โก๏ธ ์ด๋, ํ์ํ ๋ณ์์ธ id๋ฅผ ์ ๋ฌํ๋ ๋ฐฉ๋ฒ์ **`Query String`** <br/> 
ex) `๋๋ฉ์ธ/third/update/?id=3` <br/> 
<br/> 
```
//third/views.py
    elif request.method == "GET":
        # item = Restaurant.objects.get(pk=request.GET.get('id')) ## third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})
```
> ๋ง์ฝ ํด๋น id๋ฅผ ๊ฐ์ง ๊ฐ์ฒด๊ฐ ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ๋ฅผ ์ํด `get_object_or_404` ์ฌ์ฉ<br/>
> ํด๋น id์ Restaurant ๊ฐ์ฒด๋ฅผ ์๋ ฅ๋ฐ์ ๋ ์ฌ์ฉํ๋ (createํ  ๋) ํผ์ธ RestaurantForm์ ๋ค์ ๋ฐ์ ์ด<br/>
> 'third/update.html'์ ์์ ํ๊ธฐ ์ํด ํผ์ ๋ค์ ๋ด๋ ค๋ณด๋<br/>

<br/>
โก๏ธ createํ  ๋์ ํผ์ ์๋ ฅ๋ฐ๋ฏ์ด updateํ  ๋์ ํผ์ ์๋ ฅ๋ฐ์ (์์ ์ฌํญ์ด ๋ฐ๋) <br/>
```
// third/update.html
  <form action="{% url 'restaurant-update' %}" method='post'>
```

โก๏ธ 'restaurant-update'๋ผ๋ name์ ๊ฐ๋ url๋ก `POST`๋ฐฉ์์ผ๋ก ์ ๊ทผ<br/>
```
//third/views.py
    if request.method == "POST" and 'id' in request.POST:   ## ๋ง์ฝ id๊ฐ์ด ์ค์  DB์ ์๋ ๊ฐ์ด ์๋? -> listํ๋ฉด์ผ๋ก ๋์๊ฐ!
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        # ๋ง์ฝ password ๊ฐ์ด POST request ๋ฅผ ํตํด ์์ผ๋ฉด 'password'๊ฐ์ด ์์๊ฑฐ๊ณ 
        # ์๋๋ผ๋ฉด ๋ํดํธ๋ก ''๋น string
        form = UpdateRestaurantForm(request.POST, instance=item)  ## instance๋ฅผ ์ง์ ํด์ฃผ์ง ์์ผ๋ฉด create์ ๋๊ฐ์ด ๋ ์คํ ๋์ ์ ์ค๋ธ์ ํธ๋ก ์ถ๊ฐ
        if form.is_valid() and password == item.password:
            item = form.save()
```
> **์ ๊ทผ ๋ฐฉ์์ด `POST`์ด๊ณ , (?id=7)query string ๋ฐฉ์์ผ๋ก ์ ๋ฌ๋๋ 'id'๊ฐ ์ค์  DB์ ์กด์ฌํ๋ ๊ฒฝ์ฐ.**
> ๋ง์ฝ ํด๋น id๋ฅผ ๊ฐ์ง ๊ฐ์ฒด๊ฐ ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ๋ฅผ ์ํด `get_object_or_404` ์ฌ์ฉ<br/>
> ํด๋น id๋ฅผ ๊ฐ๋ Restaurant object๋ฅผ item์ ๋ฐ์ ์ด
>
> POST ๊ฐ์ฒด๋ก ๋ฐ์์จ password๊ฐ ์กด์ฌํ๋ฉด ๊ทธ๋๋ก ์ฌ์ฉ, ์์ ๊ฒฝ์ฐ ๋น string ''์ด ๊ธฐ๋ณธ <br/>
> ๋ฐ์์จ item ๊ฐ์ฒด๋ฅผ ์์ ํ ํผ(POST๋ก ๋ฐ์์จ..)์ผ๋ก ์์  --> `UpdateRestaurantForm` <br/>
> ํผ์ด ์ ํจํ๊ณ , password๊ฐ ๊ธฐ์กด์ password์ ๋์ผํ ๊ฒฝ์ฐ ํด๋น ์ค๋ธ์ ํธ๋ฅผ ํผ๋๋ก DB์ ์ ์ฅ <br/>
> ๋ง์ฝ `UpdateRestaurantForm`์์ instance๋ฅผ ํน๋ณํ ์ง์ ํด์ฃผ์ง ์๋ ๊ฒฝ์ฐ ์ ๊ฐ์ฒด๋ฅผ ์์ฑํ๋ ๊ฒ๊ณผ ๊ฐ์ -- CREATE <br/>
<br/>

โก๏ธ ๋ง์ฝ `POST๋ก ๋ฐ์์จ id`๊ฐ ์ ํจํ์ง ์์ ๊ฒฝ์ฐ, 'third/list'ํ์ด์ง๋ก ๋์๊ฐ!!!
```
    return HttpResponseRedirect('/third/list')
```
<br/><br/>
โก๏ธ ์์ ํ  ๋ ์ฌ์ฉ๋๋ ํผ
```
//third/forsm.py
class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']

```
> 'password' ์ ์ธํ๊ณ , POST๋ก ๋ฐ์์จ RestaurantForm์ ๋ฐ์์์ ์ ์ฅ

----------------------------------------

## DELETE ๐
๐ ๋ ์คํ ๋ ์ญ์  ๊ตฌํํด๋ณด๊ธฐ <br/>

**๋ ์คํ ๋ ์ญ์  ํ๋ก์ฐ** : <br/>
โก๏ธ ์์ธํ๋ฉด์ธ 'third/detail.html'์ '์ญ์ ํ๊ธฐ' ๋ฒํผ ํด๋ฆญ
```
<a href="{% url 'restaurant-delete' id=item.id %}">
```
โก๏ธ 'restaurant-delete'๋ผ๋ name์ ๊ฐ๋ url์ **GET๋ฐฉ์์ผ๋ก ์ ๊ทผ** && ์ด ๋, **Path Parameter** ๋ฐฉ์์ผ๋ก ์ด๋ค ๋ ์คํ ๋์ธ์ง `id` ์ ๋ฌ <br/>
ex) `๋๋ฉ์ธ/third/restaurant/7/delete/`<br/>
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
> **Path Parameter** ๋ฐฉ์์ผ๋ก ๋ฐ์ view ๋ฉ์๋์์ id๋ ๋งค๊ฐ๋ณ์๋ก ์ฌ์ฉ ๊ฐ๋ฅ <br/>
> `POST` ๊ฐ์ฒด์ ๋ฐ์์จ `password`๊ฐ ํด๋น id๋ฅผ ๊ฐ๋ Restaurant์ ๊ธฐ์กด password์ ์ผ์นํ๋์ง ํ์ธ <br/>
> ์ผ์นํ๋ค๋ฉด `item.delete`๋ฅผ ํตํด Restaurant object ์ญ์  <br/>
> ์ผ์นํ์ง ์๋๋ค๋ฉด, 'third/delete.html'๋ก ๋์๊ฐ. <br/>
