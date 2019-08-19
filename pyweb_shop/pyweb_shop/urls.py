from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 상품관련
    path('product_list/', views.product_list),
    path('product_write', views.product_write),
    path('product_insert', views.product_insert),
    path('product_detail', views.product_detail),
    path('product_edit', views.product_edit),
    path('product_update', views.product_update),
    path('product_delete', views.product_delete),
    # 회원 로그인 처리 관련
    path("", views.home, name="home"),
    path("join/", views.join, name="join"),
    path("login/", views.login_check, name="login"),
    path("logout/", views.logout, name="logout"),
]
