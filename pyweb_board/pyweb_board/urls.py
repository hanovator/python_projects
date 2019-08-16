from django.contrib import admin
from django.urls import path
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('download', views.download),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
    path('reply_insert', views.reply_insert),
]
