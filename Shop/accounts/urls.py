from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.Register.as_view(), name="Register"),
    path('login/', views.login, name="Login"),
    path('logout/', views.Logout.as_view(), name="Logout"),
    path("kkk/", views.Test.as_view())


]
