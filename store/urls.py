from django.urls import path
from . import views

urlpatterns = [
    path('<int:mall_id>/create/', views.create_store, name='create_store'),
    path('<int:mall_id>/', views.store_list, name='store_list'),
    path('login/', views.shop_login, name='shop_login'),
    path('shop_dashboard/', views.shop_dashboard, name='shop_dashboard'),
    path('logout/', views.store_logout, name='store_logout'),
    path('<int:mall_id>/shops/', views.shop_list, name='shop_list'),



]