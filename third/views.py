from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from django.core.paginator import Paginator
from third.forms import  RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg


# Create your views here.
def list(request):
    # Review 모델에만 restaurant로 foreignkey로 relation을 설정햇지만,
    # Restaurant 모델에도 자동으로 review (Review->review)이 relation 으로 생김
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


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST) #POST요청으로 들어온 모든 데이터를 자동으로 레스토랑폼(모델폼)에 담아서 데이터 저장
        if form.is_valid():
            new_item = form.save()  # DB에 저장
        return HttpResponseRedirect('/third/list/')

    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


def update(request):
    if request.method == "POST" and 'id' in request.POST:   ## 만약 id값이 실제 DB에 있는 값이 아님? -> list화면으로 돌아가!
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        # 만약 password 값이 POST request 를 통해 왔으면 'password'값이 왓을거고,#
        # 아니라면 디폴트로 ''빈 string
        form = UpdateRestaurantForm(request.POST, instance=item)  ## instance를 지정해주지 않으면 create와 똑같이 레스토랑의 새 오브젝트로 추가
        if form.is_valid() and password == item.password:
            item = form.save()

    elif request.method == "GET":
        # item = Restaurant.objects.get(pk=request.GET.get('id')) ## third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/list')

# path parameter로 설정하면 request와 별개로 바로 parameter을 받을 수 있음
def detail(request, id):
    if 'id' is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == "POST" and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('restaurant-detail', id=id)
    return render(request, 'third/delete.html', {'item': item})

    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list/')


def review_create(request, restaurant_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id=restaurant_id)  # 주소가 변경되더라도 (view name 기반이라서 url 바뀌더라도 ㄱㅊ)
                                                                # id는 path-parameter로 처리 (detail url은 /restaurant/<int:id>/

    # 처음엔 GET으로 접속
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})     # 사용자에게 주기 전, 미리 채워주길 원하는 부분을 initial로 줌 (어떤 레스토랑에 대한 리뷰인가를 미리 지정해줌)
    return render(request, 'third/review_create.html', {'form': form, 'item': item})    # context는 template에게 넘겨줄 값


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at')
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }
    return render(request, 'third/review_list.html', context)
