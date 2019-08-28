from django.contrib import admin
from django.conf.urls import url

from loginapp.views import LoginView
from . import views
urlpatterns = [
    url('register/', views.Register.as_view(), name='register'),
    url('success/', views.Success.as_view(), name='success'),
    url('fail/', views.Fail.as_view(), name='fail'),
    url('signup/', views.SubmitView.as_view(), name='signup'),
    url('signin/', views.LoginView.as_view(), name='login'),

]