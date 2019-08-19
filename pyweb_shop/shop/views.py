from django.shortcuts import render
import math
import os
from django.views.decorators.csrf import  csrf_exempt
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

    if "file1" in  request.FILES:
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








