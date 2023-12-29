from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('cart', views.CartView.as_view(), name='cart'),
    path('cart/<product_id>', views.CartView.as_view(), name='cart_post'),
    path('cart/delete/<order_id>', views.CartView.as_view(), name='cart_delete'),
    path('cart/buy/<order_id>', views.BuyView.as_view(), name='buy'),

]