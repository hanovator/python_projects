from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from memo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", views.home),
    url(r"^insert_memo$", views.insert_memo),
    url(r"^detail$", views.detail_memo),
    url(r"^update_memo$", views.update_memo),
    url(r"^delete_memo$", views.delete_memo),
]
