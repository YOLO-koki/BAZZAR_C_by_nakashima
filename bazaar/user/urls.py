from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.UserIndexView.as_view(),name = 'index'),#トップページ
    path('userCheck/', UserCheckView.as_view(), name='userCheck'),
    path('userRegist/', UserRegistView.as_view(), name='userRegist'),
    path('userComplete/', UserCompleteView.as_view(), name='userComplete'),
    path('userLogin/',UserLoginView.as_view(),name='userLogin'),
    path('userMailSend/',UserMailSendView.as_view(),name='userMailSend')
    ]