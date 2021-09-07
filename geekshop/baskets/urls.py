
from django.contrib import admin
from django.urls import path, include

app_name = 'baskets'

from baskets.views import basket_add, basket_remove

urlpatterns = [
   path('basket_add/<int:id>', basket_add, name='basket_add'),
   path('basket_remove/<int:id>', basket_remove, name='basket_remove'),
]
