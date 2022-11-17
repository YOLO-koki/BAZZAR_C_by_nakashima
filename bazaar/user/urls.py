from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.UserIndexView.as_view(),name = 'index'),#トップページ
    ]