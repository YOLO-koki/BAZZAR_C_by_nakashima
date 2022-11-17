from django.urls import path
from .views import TopIndexView

app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
]
