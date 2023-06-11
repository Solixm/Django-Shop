from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.LogoutView.as_view(), name='log_out'),

]
