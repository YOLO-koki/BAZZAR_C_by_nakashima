from django.urls import path
from . import views

app_name = 'comp'
urlpatterns = [
    path('', views.CompIndexView.as_view(),name = 'index'),#トップページ
    ]