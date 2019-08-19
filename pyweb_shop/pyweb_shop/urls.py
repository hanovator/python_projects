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

]
