from django.urls import path
from .views import TopIndexView
from .views import CoStoreDetailView
from .views import CoInquiryForm
from .views import TopLoginView
from .views import CoCheckInquiryInfoView
from .views import TestView

app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
    path('topdetail/',CoStoreDetailView.as_view(),name="detail"),#詳細ページ
    path('topinquiry/',CoInquiryForm.as_view(),name="inquiry"),#問い合わせ
    path('login/',TopLoginView.as_view(),name="login"),#ログインページ
    path('test/<str:userid>',TestView.as_view(),name="test"),#テストページ
    path('topcheckinquiry/',CoCheckInquiryInfoView.as_view(),name="checkinquiry"),#問い合わせ内容確認
]