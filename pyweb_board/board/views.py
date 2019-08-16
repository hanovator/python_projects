from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt
import os
from board.models import Board, Comment
from django.shortcuts import render_to_response, redirect

UPLOAD_DIR = 'd:/upload/'


@csrf_exempt
def list(request):
    try:
        search_option = request.POST['search_option']
    except:
        search_option = 'writer'
    try:
        search = request.POST['search']
    except:
        search = ''

    if search_option == 'all':
        boardCount = Board.objects.filter(Q(writer__contains = search) | Q(title__contains = search) | Q(content__contains = search)).count()
        boardList = Board.objects.filter(Q(writer__contains = search) | Q(title__contains = search) | Q(content__contains = search)).order_by('-idx')
    elif search_option == 'writer':
        boardCount = Board.objects.filter(Q(writer__contains=search)).count()
        boardList = Board.objects.filter(Q(writer__contains=search)).order_by('-idx')
    elif search_option == 'title':
        boardCount = Board.objects.filter(Q(title__contains=search)).count()
        boardList = Board.objects.filter(Q(title__contains=search)).order_by('-idx')
    elif search_option == 'content':
        boardCount = Board.objects.filter(Q(content__contains=search)).count()
        boardList = Board.objects.filter(Q(content__contains=search)).order_by('-idx')

    return render_to_response('list.html', {'boardList': boardList, 'boardCount': boardCount, 'search_option': search_option, 'search': search})


def write(request):
    return render_to_response('write.html')


@csrf_exempt
def insert(request):
    fname = ''
    fsize = 0
    if 'file' in request.FILES:  # 첨부파일 태그의 이름이 file인 태그가 있다면
        file = request.FILES['file']  # 파일 객체를 받아온다.
        fname = file._name
        fp = open('%s%s' % (UPLOAD_DIR, fname), 'wb')  # 이진파일 저장 모드로 오픈
        for chunk in file.chunks():  # 파일 조각을 조금씩 받아서 서버에 저장
            fp.write(chunk)
        fp.close()
        fsize = os.path.getsize(UPLOAD_DIR + fname)

    dto = Board(writer=request.POST['writer'],
                title=request.POST['title'],
                content=request.POST['content'],
                filename=fname,
                filesize=fsize)
    dto.save()
    return redirect('/')


def download(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR + dto.filename
    filename = os.path.basename(path)
    filename = urlquote(filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')  # mime type(파일의 종류를 범용적으로 설정)
        response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(filename)
        dto.down_up()
        dto.save()
        return response


def detail(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    filesize = "%.2f" % (dto.filesize / 1024)
    #댓글 목록
    commentList = Comment.objects.filter(board_idx=id).order_by('idx')

    return render_to_response('detail.html', {'dto': dto, 'filesize': filesize, 'commentList': commentList})


@csrf_exempt
def update(request):
    id = request.POST['idx']
    dto_src = Board.objects.get(idx=id)

    fname = dto_src.filename  # 첨부파일을 바꾸지 않았을경우대비
    fsize = dto_src.filesize

    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file._name
        fp = open('%s%s' % (UPLOAD_DIR, fname), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        fsize = os.path.getsize(UPLOAD_DIR + fname)

    dto_new = Board(idx=id, writer=request.POST['writer'], title=request.POST['title'], content=request.POST['content'], filename=fname, filesize=fsize)
    dto_new.save()
    return redirect('/')


@csrf_exempt
def delete(request):
    id = request.POST['idx']
    Board.objects.get(idx=id).delete()
    return redirect('/')


@csrf_exempt
def reply_insert(request):
    id = request.POST['idx']
    dto = Comment(board_idx=id, writer=request.POST['writer'], content=request.POST['content'])
    dto.save()
    return HttpResponseRedirect('detail?idx=' + id)







