
from django.contrib import admin
from django.urls import path, include

app_name = 'admins'

from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView
from admins.views import admin_category,  admin_category_create, admin_category_update, admin_category_delete
from admins.views import admin_products, admin_products_create, admin_products_update, admin_products_delete

urlpatterns = [
   path('', index, name='index'),
   # path('users/', admin_users, name='admin_users'),
   path('users/', UserListView.as_view(), name='admin_users'),
   # path('user-create', admin_users_create, name='admin_users_create'),
   path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
   # path('user-update/<int:id>', admin_users_update, name='admin_users_update'),
   path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
   path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

   path('category/', admin_category, name='admin_category'),
   path('category-create/', admin_category_create, name='admin_category_create'),
   path('category-update/<int:id>', admin_category_update, name='admin_category_update'),
   path('category-delete/<int:id>', admin_category_delete, name='admin_category_delete'),

   path('products/', admin_products, name='admin_products'),
   path('products-create/', admin_products_create, name='admin_products_create'),
   path('products-update/<int:id>', admin_products_update, name='admin_products_update'),
   path('products-delete/<int:id>', admin_products_delete, name='admin_products_delete'),
]
