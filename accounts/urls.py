from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup', views.Register.as_view(), name="Register"),
    path('login', views.login, name="Login"),
    path('logout/', views.Logout.as_view(), name="Logout"),
    path('verify', views.VerifyView.as_view(), name='verify'),
    path('forgot', views.ForgotPasswordView.as_view(), name='forgot'),
    path('forgotlogin', views.ForgotLogin.as_view(), name='forgot_login'),
    path("kkk/", views.Test.as_view())


]
