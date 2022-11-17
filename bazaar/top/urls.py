from django.urls import path
from .views import TopIndexView
from .views import CoStoreDetailView

app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
    path('detail',CoStoreDetailView.as_view(),name="detail")
]
