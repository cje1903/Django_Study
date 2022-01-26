from django.shortcuts import render
from django.http import HttpResponseRedirect
from second.models import Post
# model에서 정의한 Post라는 클래스를 가져오기 (클래스 - 테이블 개념)
from second.forms import PostForm


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    # POST로 접속
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form)  # 레코드를 생성하는 코드 필요
            new_item = form.save()  # 이 구문 하나면, 모델 스키마에 저장
        return HttpResponseRedirect('/second/list/')

    # GET 으로 접속
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')
