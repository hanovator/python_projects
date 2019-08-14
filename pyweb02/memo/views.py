from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from memo.models import Memo


def home(request):
    memoList = Memo.objects.order_by("-idx")
    print(memoList)
    memoCount = Memo.objects.all().count()
    return render_to_response("list.html", {"memoList": memoList, "memoCount": memoCount})


@csrf_exempt
def insert_memo(request):
    # 사용자가 post 방식으로 입력한 writer, memo 변수값으로 객체가 만들어짐
    memo = Memo(writer=request.POST["writer"], memo=request.POST["memo"])
    # 내부적으로 insert 명령어가 호출되어 테이블 레코드가 저장됨
    memo.save()
    return redirect("/")


def detail_memo(request):
    id = request.GET['idx']
    dto = Memo.objects.get(idx=id)
    return render_to_response("detail.html", {"dto": dto})


@csrf_exempt
def update_memo(request):
    id = request.POST['idx']
    memo = Memo(idx=id, writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect("/")


@csrf_exempt
def delete_memo(request):
    id = request.POST['idx']
    Memo.objects.get(idx=id).delete()
    return redirect("/")
