from django.shortcuts import render
import math
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlquote
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from shop.models import Product, Cart
from shop.forms import UserForm, LoginForm

UPLOAD_DIR = 'D:/learn/pyweb/pyweb_shop/shop/static/images/'


def product_list(request):
    count = Product.objects.count()
    productList = Product.objects.order_by('product_name')
    return render_to_response('product_list.html', {'productList': productList, 'count': count})


def product_write(request):
    return render_to_response('product_write.html')


@csrf_exempt
def product_insert(request):
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        fp = open('%s%s' % (UPLOAD_DIR, file_name), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name = '-'

    dto = Product(product_name=request.POST['product_name'],
                  description=request.POST['description'],
                  price=request.POST['price'],
                  picture_url=file_name)
    dto.save()
    return redirect('/product_list')


def product_detail(request):
    pid = request.GET['product_id']
    dto = Product.objects.get(product_id=pid)
    return render_to_response('product_detail.html', {'dto': dto, 'range': range(1, 21)})


def product_edit(request):
    pid = request.GET['product_id']
    dto = Product.objects.get(product_id=pid)
    return render_to_response('product_edit.html', {'dto': dto})


@csrf_exempt
def product_update(request):
    id = request.POST["product_id"]
    dto_src = Product.objects.get(product_id=id)
    p_url = dto_src.picture_url

    if "file1" in request.FILES:
        file = request.FILES["file1"]
        p_url = file._name
        fp = open("%s%s" % (UPLOAD_DIR, p_url), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    # 수정할 내용
    dto_new = Product(product_id=id,
                      product_name=request.POST["product_name"],
                      price=request.POST["price"],
                      description=request.POST["description"],
                      picture_url=p_url)
    dto_new.save()
    return redirect("/product_list")


@csrf_exempt
def product_delete(request):
    Product.objects.get(product_id=request.POST["product_id"]).delete()
    return redirect("/product_list")


def home(request):
    if not request.user.is_authenticated:
        data = {"username": request.user, "ist_authenticated": request.user.is_authenticated}
    else:
        data = {"last_login": request.user.last_login,
                "username": request.user.username,
                "password": request.user.password,
                "is_authenticated": request.user.is_authenticated}
    return render(request, "index.html", context={"data": data})


# 회원가입 처리
@csrf_exempt
def join(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            django_login(request, new_user)
            return redirect('/')
        else:
            return render_to_response('index.html', {'msg': '회원가입 실패... 다시 시도해 보세요'})
    else:
        form = UserForm()
        return render(request, 'join.html', {'form': form})


# 로그인 처리 함수
@csrf_exempt
def login_check(request):
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=name, password=pwd)  # 아이디, 비번이 맞는지 확인
        if user is not None:
            django_login(request, user)
            request.session['userid'] = name  # 세션변수를 생성(로그인여부 판단)
            return redirect('/')
        else:
            return render_to_response('index.html', {'msg': '로그인실패... 다시 시도해 보세요'})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout(request):
    # django에 내장된 로그아웃 처리 함수
    django_logout(request)
    # 세션변수에 저장된 모든값드릉ㄹ 삭제
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return redirect('/')