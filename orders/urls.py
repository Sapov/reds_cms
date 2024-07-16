from django.urls import path
from .views import orders, new_order, view_orders

app_name = 'orders'

urlpatterns = [
    path('', orders, name='orders'),
    path('', new_order, name='new_order'),
    path('', view_orders, name='view_orders')
]
