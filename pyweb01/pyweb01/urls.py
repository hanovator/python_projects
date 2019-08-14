from django.contrib import admin
from django.conf.urls import url
from bookmark import views

# url pattern 정의
# r : 정규표현식, ^ start, $ end
urlpatterns = [
    # http://localhost/admin
    url(r'^admin/', admin.site.urls),
    # http://localhost
    url(r"^$", views.home),
    # http://localhost/detail
    url(r"^detail$", views.detail)
]
