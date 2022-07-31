
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserSignUpView, name='signup'),
    path('signin/', views.UserSignInView, name='signin'),
    path('otp/', views.OtpView, name='otp')
]