from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.UserIndexView.as_view(),name = 'index'),#トップページ
    path('userCheck/', views.UserCheckView.as_view(), name='userCheck'),
    path('userRegist/', views.UserRegistView.as_view(), name='userRegist'),
    path('userComplete/', views.UserCompleteView.as_view(), name='userComplete'),
    path('userLogin/',views.UserLoginView.as_view(),name='userLogin'),
    path('userMailSend/',views.UserMailSendView.as_view(),name='userMailSend')
    ]