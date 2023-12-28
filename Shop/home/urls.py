from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include


app_name = 'home'

# router = DefaultRouter()
# router.register(r'', views.home, basename='home')
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('<str:category>/', views.home.as_view(), name='product_category')
]
