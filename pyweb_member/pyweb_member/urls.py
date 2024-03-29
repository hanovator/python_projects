from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout, name='logout'),
]
