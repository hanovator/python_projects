from bookmark.models import Bookmark
from django.shortcuts import render_to_response


def home(request):
    # bookmark 테이블의 모든 레코드가 title 순으로 리스트에 저장
    urlList = Bookmark.objects.order_by("title")
    # bookmark 테이블의 레코드갯수
    urlCount = Bookmark.objects.all().count()
    # list.html로 넘어가서 출력, {key:value}구조로 데이터가 전달됨
    return render_to_response("list.html", {"urlList": urlList, "urlCount": urlCount})


def detail(request):
    # get 방식으로 넘어온 변수 조회
    addr = request.GET['url']
    # bookmark 테이블에서 url에 해당하는 레코드를 조회
    dto = Bookmark.objects.get(url=addr)
    # detail.html로 넘어가서 출력됨.
    return render_to_response("detail.html", {"dto": dto})
