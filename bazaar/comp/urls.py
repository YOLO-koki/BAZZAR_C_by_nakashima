from django.urls import path
from .views import CompIndexView
from .views import CompMypageView


app_name = 'comp'
urlpatterns = [
    path('', CompIndexView.as_view(), name='index'),  # トップページ
    path('mypage/',CompMypageView.as_view(), name='mypage'),  # マイページ
]
