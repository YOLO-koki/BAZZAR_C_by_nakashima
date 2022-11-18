from django.urls import path
from .views import TopIndexView
from .views import CoStoreDetailView
from .views import CoInquiryView

app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
    path('topdetail/',CoStoreDetailView.as_view(),name="detail"),
    path('topinquiry/',CoInquiryView.as_view(),name="inquiry"),
]