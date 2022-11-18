from django.urls import path
from . import views

app_name = 'comp'
urlpatterns = [
    path('', views.CompIndexView.as_view(), name='index'),  # トップページ
    path('mypage/', views.CompMypageView.as_view(), name='mypage'),  # マイページ
]
