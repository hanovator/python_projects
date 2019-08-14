from django.contrib import admin
from memo.models import Memo


# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display = ("writer", "memo")


# 관리자 사이트에 Memo class와 MemoAdmin class를 등록
admin.site.register(Memo, MemoAdmin)
