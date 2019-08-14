from django.contrib import admin
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    # 관리자 화면에 출력할 필드목록
    list_display = ('title', 'url')

# 관리자 페이지에 Bookmark와 BookmarkAdmin 클래스를 등록함
admin.site.register(Bookmark, BookmarkAdmin)