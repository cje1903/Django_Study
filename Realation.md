__Realation ๐__
=================
> * **Relation**์ ๋ชจ๋ธ๊ณผ ๋ชจ๋ธ ๊ฐ์ ์ข์ ๊ด๊ณ <br/><br/>
> * **Many-to-Many** - ex) ์ถํ์ฌ์ ์ ์๋ฌผ์ ๊ด๊ณ (ํ๋์ ์ถํ์ฌ์์ ์ฌ๋ฌ ๊ฐ์ ์ ์๋ฌผ, ํ๋์ ์ ์๋ฌผ์ ์ฌ๋ฌ ๊ฐ์ ์ถํ์ฌ์์ OK)
> * **Many-to-One** - ex) ๊ฒ์๊ธ๊ณผ ๋๊ธ์ ๊ด๊ณ (ํ๋์ ๊ฒ์๊ธ์ ์ฌ๋ฌ ๊ฐ์ ๋๊ธ)
> * **One-to-One** - ex) ์ฌ๊ถ๊ณผ ์ฌ๋์ ๊ด๊ณ (ํ ์ฌ๋์ ํ๋์ ์ฌ๊ถ, ํ๋์ ์ฌ๊ถ์ ํ ์ฌ๋์๊ฒ๋ง.)
--------------------------
### **`Restaurant`** ๋ชจ๋ธ๊ณผ **`Review`** ๋ชจ๋ธ์ **Many-to-One** ๊ด๊ณ!!
<img src="https://user-images.githubusercontent.com/86587287/168635497-5d0b36f8-fc49-4e9f-82f4-f27992211aeb.png" width="650px">

```
//third/models.py
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)
    # ๋ง์ฝ default ์์ฑ์ ์ง์ ํ์ง ์์ผ๋ฉด, ๊ธฐ์กด์ ์๋ ๊ฐ๋ค์๋ password ๊ฐ์ด ์ ๋ค์ด ์์
    # ๊ธฐ์กด ๊ฒ๋ค์ password ์์ฑ์ Null,
    # ์๋ ์ด๋ ํ ์์ฑ์ ์ ์ํ  ๋, null์ ์ง์ ํด์ฃผ์ง ์์ผ๋ฉด ๊ธฐ๋ณธ์ ์ผ๋ก null์ด๋ฉด ์๋๊ณ  ๋ฌด์กฐ๊ฑด ์ฑ์์ ธ์ผ ํจ
    # 1๋ฒ ํ์๋น ๊ฐ๋จ [ ]
    # 2๋ฒ ์ผ์๋น ๊ฐ๋ถ [ ]
    image = models.CharField(max_length=500, default=None, null=True)
    # ์ด๋ฏธ์ง์ url์ ๋ฃ์ ๊ฑฐ์ด๊ธฐ ๋๋ฌธ์ ๋ฌธ์์ฌ(string)์ผ๋ก ์ค์  - CharField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # ํ๊ฐ์ ๋ ์คํ ๋ - ์ฌ๋ฌ๊ฐ์ ๋ฆฌ๋ทฐ Many to One
    # ์ฌ๋ฌ๊ฐ์ธ ๋ฆฌ๋ทฐ์์ ๋ ์คํ ๋ ์ ์ธ
    # Restaurant์ pk๊ฐ์ ๊ฐ์ ธ์ด (pk=3๋ฒ ๋ ์คํ ๋์ ๋ํ ๋ฆฌ๋ทฐ์๋๋ค~)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
> * `Review`์์ Restaurant๋ฅผ ForeignKey๋ก ์ฐธ์กฐํ  ๋, `์ฐธ์กฐ๋ฌด๊ฒฐ์ฑ`์ ์ํด `on_delete`์ต์์ด ๋ถ๋๋ค. <br/>
> `on_delete`๋ ForeignKeyField๊ฐ ๋ฐ๋ผ๋ณด๋ `Restaurant์ ๊ฐ์ฒด๊ฐ ์ญ์ ๋  ๋`, ์ฒ๋ฆฌ ๋ฒ <br/>
>
> **`CASCADE`**: ForeignKeyField๋ฅผ ํฌํจํ๋ Review ๋ชจ๋ธ ์ธ์คํด์ค ๋ชฝ๋ ์ญ์  <br/>
> **`PROTECT`**: ํด๋น ์์(restaurant field)๊ฐ ๊ฐ์ด ์ญ์ ๋์ง ์๋๋ก Protected Error์ ๋ฐ์์ํจ๋ค. <br/>
> **`SET_NULL`**: ForeignKeyField(restaurant)๊ฐ์ NULL๋ก ๋ฐ๊พผ๋ค. (null=True์ผ ๋๋ง ์ฌ์ฉ ๊ฐ๋ฅ) <br/>
> **`SET_DEFAULT`**: default ๊ฐ์ผ๋ก ๋ณ๊ฒฝํ๋ค.
> **`SET`**: SET์ ์ค์ ๋ ํจ์์ ์ํด ์ค์ 
> **`DO_NOTHING`**: ์๋ฌด๊ฒ๋ ํ์ง ์์. (์ฐธ์กฐ ๋ฌด๊ฒฐ์ฑ์ ํด์น  ์ ์์ด์ ์ ์ฌ์ฉ X)


<br/>

* Restaurant ๋ชจ๋ธ์ primary key์ธ id๋ migration ๊ณผ์ ์์ ์๋์ผ๋ก ์์ฑ๋๋ ๊ฐ์<br/>
* `id`๋ models.py์์ ์ ์ํด์ค ์  ์๋ field ์ด์ง๋ง ์์ฑ๋์ด์์
```
// migration/0002_review.py
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
```

