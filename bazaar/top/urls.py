from django.urls import path
from .views import TopIndexView
from .views import CoStoreDetailView
from .views import TopLoginView

app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
    path('login/',TopLoginView.as_view(),name="login"),#ログインページ
    path('detail/',CoStoreDetailView.as_view(),name="detail"),
]
