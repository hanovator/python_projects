from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from member.forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout)


def home(request):
    if not request.user.is_authenticated:
        data = {'username': request.user,
                'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login,
                'username': request.user.username,
                'password': request.user.password,
                'is_authenticated': request.user.is_authenticated}

    return render(request, 'index.html', context={'data': data})


# 회원가입 처리함수
@csrf_exempt
def join(request):
    if request.method == 'POST':
        form = UserForm(request.POST)  # 사용자가 입력한 회원가입 폼 데이터
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)  # form.cleaned_data 검증에 성공한 값들로 User 인스턴스 생성
            django_login(request, new_user)  # 내장된 로그인 처리
            return render_to_response('index.html', {'msg': '회원가입이 되었습니다.'})
        return render_to_response('index.html', {'msg': '회원가입 실패... 다시 시도해 보세요.'})
    else:
        form = UserForm()  # 회원가입 폼 인스턴스 생성
        return render(request, 'join.html', {'form': form})  # 회원 가입페이지로 이동


def logout(request):
    django_logout(request)
    return redirect('/')


def login_check(request):
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=name, password=pwd)
        if user is not None:
            django_login(request, user)
            return redirect('/')
        else:
            return render_to_response('index.html', {'msg': '로그인실패...'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
