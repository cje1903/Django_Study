__second__ ๐
===========
## __second ์น ์ฑ์ ๋๋ ํ ๋ฆฌ ๊ตฌ์กฐ__ ๐ <br/>
```
โโ๐second
โ  โโ๐migrations
โ  โโ๐templates
โ  โ  โโ๐ฟsecond
โ  โ    โโbase.html
โ  โ    โโlist.html
โ  โ    โโcreate.html
โ  โ    โโconfirm.html
โ  โโ__init__.py
โ  โโadmin.py
โ  โโapps.py
โ  โโforms.py
โ  โโmodels.py
โ  โโtests.py
โ  โโurls.py
โ  โโviews.py
```

## __`models.py` & `forms.py`__ ๐ <br/>

### ๐ `models.py`<br/>
> `models.py`์ `Post` ๋ผ๋ ํด๋์ค(ํ์ด๋ธ) ์์ฑ _(์์ฑ - title, content, created_at, updated_at)_
```
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()    # ๋ฌธ์์ด ๊ธธ์ด ์ ์ x

    created_at = models.DateTimeField(auto_now_add=True)    # ์๋์ผ๋ก ํ์ฌ ์๊ฐ ๊ธฐ๋ก
    updated_at = models.DateTimeField(auto_now=True)    # ์์ ๋  ๋๋ง๋ค ์ต๊ทผ ์์ ์๊ฐ ๊ธฐ๋ก
```
> database๋ default๋ก `sqlite3`๋ฅผ ์ฌ์ฉ <br/>
> `python manage.py makemigrations` => ๋ณ๊ฒฝ ์ฌํญ์ ๋ํ ๋ง์ด๊ทธ๋ ์ด์ ํ์ผ(0001_initial, 0002_alter_title_max_length ์ ๊ฐ์ด ๋ณ๊ฒฝ ์ฌํญ์ด ํ์ผ๋ช์ ํ์ ๋จ) ์์ฑ<br/>
> `python manage.py migrate` => ๋ณ๊ฒฝ ์ฌํญ์ ๋ฐ์ดํฐ ๋ฒ ์ด์ค์ ์ ์ฉ<br/>

<br/>

### ๐ `forms.py`<br/>
```
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('์ ๋ชฉ'),
            'content': _('๋ด์ฉ')
        }
        help_texts = {
            'title': _('์ ๋ชฉ์ ์๋ ฅํด์ฃผ์ธ์ฉ(*๏ฟฃ3๏ฟฃ)โญ'),
            'content': _('๋ด์ฉ์ ์๋ ฅํด์ฃผ์ธ์ฉ(*๏ฟฃ3๏ฟฃ)โญ')
        }
        error_message = {
            'name': {
                'max_length': _("์ ๋ชฉ์ด ๋๋ฌด ๊น๋๋ค. 30์ ์ดํ๋ก ํด์ฃผ์ธ์")
            }
        }

```
> __`Form`์ด ์๋ `ModelForm`์ ์ฌ์ฉํ๋ ์ด์ __ <br/>
> ๋ชจ๋ธ `Post`์ ์์ฑ์ด ์ถ๊ฐ๋๋ฉด `Form`๋ ๊ทธ ๋๋ง๋ค ์์ ํด ์ฃผ์ด์ผ ํ๊ณ <br/>
> form์ผ๋ก ๋ฐ์๋ ๋ฐ์ดํฐ๋ค์ ๋ค์ ๊บผ๋ด์ ์์ ๋ Post ๋ชจ๋ธ ํด๋์ค์ ์ธ์คํด์ค์ ๋ฃ์ด์ฃผ์ด์ผ ํ๊ธฐ ๋๋ฌธ์ ๋ฒ๊ฑฐ๋ก์<br/>
> โ Django๋ `Model form`์ผ๋ก ์ด ๋ฒ๊ฑฐ๋ก์์ ํด๊ฒฐ โ <br/>


## __URL Patterns__ ๐ <br/>

### ๐ `http://127.0.0.1:8000/second/list/`<br/>
<img src="https://user-images.githubusercontent.com/86587287/167896152-53151854-6a19-44a2-a034-85c565dc2f69.png" width="400px">

```
//views.py
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)
```
> Post ํด๋์ค์ ๋ชจ๋  ์ค๋ธ์ ํธ๋ค ๊ฐ์ ธ์ด -> `templates/second/list.html`๋ก ๋ฐ์ดํฐ(context ํํ)๋ฅผ ๋๊ธฐ๊ฒ ๋ค<br/>
> ์ค๋ธ์ ํธ๋ค์ `title`, `content` ์์ฑ์ ํ๋ฉด์ ์ถ๋ ฅ<br/>
```
// templates/second/list.html
<a href="{% url 'create' %}" style="background-color:lightgray">์๋ ฅํ๋ฌ ๊ฐ๊ธฐ</a>
```
> a ํ๊ทธ๋ฅผ ๋๋ฅด๋ฉด `'create'๋ผ๋ name์ url`๋ก ์ด๋ํ๊ฒ ๋ค => `http://127.0.0.1:8000/second/create/`

<br/>

### ๐ `http://127.0.0.1:8000/second/create/`<br/>
1๏ธโฃ `GET์ผ๋ก 'create'์ ์ ๊ทผ` <br/><br/>
<img src="https://user-images.githubusercontent.com/86587287/167896209-ebf180b8-6685-4a42-a205-29ec079ab2ee.png" width="400px">

```
// views.py
def create(request):
    # GET ์ผ๋ก ์ ์
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})
```
> * `http://127.0.0.1:8000/second/list/`์์ '์๋ ฅํ๋ฌ ๊ฐ๊ธฐ'๋ฅผ ํด๋ฆญํด์ ์ ๊ทผ <br/>
> * url์ฐฝ์ `http://127.0.0.1:8000/second/create/`๋ฅผ ์ง์  ์ณ์ ์ ๊ทผ <br/>
> 
> ๋ฐ์ดํฐ๋ฅผ ์๋ ฅ๋ฐ๊ธฐ ์ํด `PostForm`(ModelForm) __๋น ๊ฐ์ฒด__ ๋ฅผ ๋ง๋ค๊ณ  'form'์ด๋ผ๋ ์ด๋ฆ์ผ๋ก 'second/create.html'๋ก ์ ๋ฌ <br/>
> title๊ณผ content๋ฅผ ์๋ ฅ๋ฐ์ ์ ์๋๋ก `templates/second/create.html`๋ฅผ render <br/>

```
// templates/second/create.html
<form action="{% url 'create' %}" method="post">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
  </table>
  <button type="submit">์ ์ถ</button>
</form>
```

> ์์ฑ๋ form์ ๋ฐ์ดํฐ๋ `'create'๋ผ๋ name์ url` ๋ก ์ ๋ฌ๋  ๊ฒ์ด๋ค, http ์์ฒญ ๋ฐฉ์์ `POST`์ด๋ค. <br/>
> _( first web app์์์ 'templates/first/select/'์์ formํ๊ทธ๋ก ์ ๋ฌํ ๋ฐ์ดํฐ number์ view๋ก์ง์ผ๋ก ์ฒ๋ฆฌํ๊ณ  ๋๋๊ธฐ ๋๋ฌธ์(DB์ ์ ์ฅํ  ํ์ X) forms.py๊ฐ ํ์ X )_<br/>

<br/>
2๏ธโฃ `POST์ผ๋ก 'create'์ ์ ๊ทผ`<br/><br/>
<img src="https://user-images.githubusercontent.com/86587287/167907849-bc347f51-d0fc-4931-a6f4-d3c761daecbe.png" width="400px">

```
def create(request):
    # POST๋ก ์ ์
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form)  # ๋ ์ฝ๋๋ฅผ ์์ฑํ๋ ์ฝ๋ ํ์
            new_item = form.save()  # ์ด ๊ตฌ๋ฌธ ํ๋๋ฉด, ๋ชจ๋ธ ์คํค๋ง์ ์ ์ฅ
        return render(request, 'second/confirm.html', {'form': form})
```
> * `templates/second/create.html`์ form์ ์ ์ถํ๋ฉด `'create'๋ผ๋ name์ url๋ก POST ๋ฐฉ์`์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ์ ๋ฌ, ๊ทธ ๋ ์ ๊ทผ<br/>

```
//templates/second/create.html
<form action="{% url 'create' %}" method="post">
```
> `request` ๊ฐ์ฒด์์ `PostForm`์ ์ ๋ฌ๋ฐ๋๋ค<br/>
> ๋ฐ์ PostForm์ด ์ ํจํ์ง ๊ฒ์ฌ ํ, ํด๋น ๋ ์ฝ๋๋ฅผ `Post ๋ชจ๋ธ์ save`ํด์ค๋ค.<br/>
> ๋ฐ์ PostForm์ ๋ณด์ฌ์ฃผ๋ `templates/second/confirm.html`์ render<br/>


## __๊ทธ ์ธ ์ค๋ช__ ๐ <br/>
โ๏ธ MTV ํจํด <br/>
> `Model`(models.py) ๋ฐ์ดํฐ ๊ฐ์ฒด ์ ์& ๋ฐ์ดํฐ<br/>
> -> `View`(views.py) ๋ฐ์ดํฐ ๊ฐ๊ณต ํ ํํ๋ฆฟ์ ์ ๋ฌ<br/>
> -> `Template`(templates/*.html) ์ฌ์ฉ์ ํ๋ฉด์ ์ถ๋ ฅ<br/>

> `Model`: class Post ์ ์<br/>
> `View`: ๋ฐ์ดํฐ๋ฅผ ์๋ ฅ๋ฐ๊ณ  ๋ก์ง์ฒ๋ฆฌ <br/>
> `Template`: View์์ ๋๊ฒจ์ค ๋ฐ์ดํฐ๋ฅผ ํ๋ฉด์ ์ถ๋ ฅ <br/>


โ๏ธ http ์์ฒญ~์๋ต ํ๋ฆ <br/>
> 1. ํด๋ผ์ด์ธํธ๊ฐ ์ฃผ์๋ก `request`์ ๋ณด๋ธ๋ค<br/>
> 2. ์ฅ๊ณ  ์น ์ฑ์ ๋ค์ด์จ ์์ฒญ์ `url`์ ํ์ธ<br/>
> 3. `urls.py`: ํด๋น url ๋ด๋น `view๋ก ์ ๋ฌ`<br/>
> 4. `view์ ๋ก์ง ์คํ` (ํ์์, model๋ก ๋ฐ์ดํฐ ์ฒ๋ฆฌ) ํ `template๋ก ์ ๋ฌ`<br/>
> 5. `template`: ์ต์ข `html ์์ฑ`<br/>
> 6. ํด๋ผ์ด์ธํธ์๊ฒ `response`<br/>
