from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('get_orders',views.get_orders, name='getOrders'),
    path('get_orders/<int:id>',views.get_orders,name='getorder')
]

urlpatterns = format_suffix_patterns(urlpatterns)