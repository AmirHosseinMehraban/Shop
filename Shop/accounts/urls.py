from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.Register.as_view(), name="Register"),


]
