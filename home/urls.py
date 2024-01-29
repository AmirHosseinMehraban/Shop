from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include


app_name = 'home'

# router = DefaultRouter()
# router.register(r'', views.home, basename='home')
urlpatterns = [
    path('', views.home.as_view(), name='Home'),
    path('<str:category>/', views.home.as_view(), name='Product_Category'),
    path('product/<str:name>', views.ProductDetailView.as_view(), name="Product_Detail"),
    path('a/b/b', views.test.as_view()),
]
