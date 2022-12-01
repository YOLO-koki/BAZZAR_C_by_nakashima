from django.urls import path
from .views import CompIndexView
from .views import CompMypageView
from .views.bo_check_infoviews import CheckRegiInfoView
from .views.bo_regist_views import CreateAccountView
from .views.bo_mail_sendviews import BoMailSendView
from .views.bo_loginviews import BoLoginView
app_name = 'comp'
urlpatterns = [
    path('', CompIndexView.as_view(), name='index'),  # トップページ
    path('mypage/',CompMypageView.as_view(), name='mypage'),  # マイページ
     path('boCheck/', CheckRegiInfoView.as_view(), name='boCheck'),
    path('boRegist/', CreateAccountView.as_view(), name='boRegist'),#新規登録
    path('boMailSend/',BoMailSendView.as_view(),name='boMailSend'),
     path('boLogin/',BoLoginView.as_view(),name='boLogin'),
]
