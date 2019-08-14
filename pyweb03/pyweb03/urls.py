from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from survey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", views.main),
    url(r"^save_survey$", views.save_survey),
    url(r"^show_result$", views.show_result),
]

# 디버깅 관련 url settings.py에 debug_toolbar를 사용하기로 설정이 되어있으면
if settings.DEBUG:
    import debug_toolbar
    # url 패턴에 debug_toolbar에서 제공하는 url을 추가함
    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]

