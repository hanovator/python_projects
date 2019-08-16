from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from guestbook.models import Guestbook
from django.shortcuts import render_to_response
from django.db.models import Q


@csrf_exempt
def list(request):
    try:
        searchkey = request.POST['searchkey']
    except:
        searchkey = ''

    try:
        search = request.POST['search']
    except:
        search = ''

    try:
        msg = request.GET['msg']
    except:
        msg = ''

    if msg == 'error':
        msg = '비밀번호가 일치하지 않습니다.'

    gbCount = Guestbook.objects.count()
    gbList = Guestbook.objects.order_by("-idx")[:]  # [:] 리스트의 처음부터 끝까지

    if searchkey == 'name_content':
        gbCount = Guestbook.objects.filter(
            Q(name__contains = search) | Q(content__contains = search)
        ).count()
        gbList = Guestbook.objects.filter(
            Q(name__contains=search) | Q(content__contains=search)
        ).order_by('-idx')
    elif searchkey == 'name':
        gbCount = Guestbook.objects.filter(
            Q(name__contains=search)
        ).count()
        gbList = Guestbook.objects.filter(
            Q(name__contains=search)
        ).order_by('-idx')
    elif searchkey == 'content':
        gbCount = Guestbook.objects.filter(
            Q(content__contains=search)
        ).count()
        gbList = Guestbook.objects.filter(
            Q(content__contains=search)
        ).order_by('-idx')

    return render_to_response('list.html', {'gbList': gbList, 'gbCount': gbCount, 'msg': msg, 'searchkey': searchkey, 'search': search})


def write(request):
    return render_to_response('write.html')


@csrf_exempt
def insert(request):
    dto = Guestbook(name=request.POST['name'],
                    email=request.POST['email'],
                    passwd=request.POST['passwd'],
                    content=request.POST['content'], )
    dto.save()
    return redirect('/')


@csrf_exempt
def passwd_check(request):
    id = request.POST['idx']
    pwd = request.POST['passwd']
    dto = Guestbook.objects.get(idx=id)
    if dto.passwd == pwd:
        return render_to_response('edit.html', {'dto': dto})
    else:
        return redirect('/?msg=error')


@csrf_exempt
def update(request):
    id = request.POST['idx']
    dto = Guestbook(idx=id, name=request.POST['name'],
                    email=request.POST['email'],
                    passwd=request.POST['passwd'],
                    content=request.POST['content'],)
    dto.save()
    return redirect('/')


@csrf_exempt
def delete(request):
    id = request.POST['idx']
    Guestbook.objects.get(idx=id).delete()
    return redirect('/')


















