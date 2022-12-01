from django.urls import path
from .views import (
    CompLoginView,
    CompSignupView,
    CompCheckRegistedInfoView,
    CompSendURLView,
    CompResetPasswordView,
    CompUpdatePasswordView,
    CompMypageView,
    CompReservationListView,
    CompReservationDetailView,)
from .views.bo_check_infoviews import CheckRegiInfoView
from .views.bo_regist_views import CreateAccountView
from .views.bo_mail_sendviews import BoMailSendView
from .views.bo_loginviews import BoLoginView
app_name = 'comp'
urlpatterns = [
    path('mypage/<str:userid>', CompMypageView.as_view(), name='mypage'),  # マイページ
    path('login/', CompLoginView.as_view(), name='login'),  # ログイン機能
    path('signup/', CompSignupView.as_view(), name='signup'),  # 新規登録機能
    path('check_registed_info/', CompCheckRegistedInfoView.as_view(), name='check_registed_info'),  # 登録内容確認
    path('send_url/', CompSendURLView.as_view(), name='send_url'),  # URL送信案内
    path('reset_password/', CompResetPasswordView.as_view(), name='reset_password'),  # パスワードリセットURL送信
    path('update_password/', CompUpdatePasswordView.as_view(), name='update_password'),  # パスワード更新
    path('reservation_list/', CompReservationListView.as_view(), name='reservation_list'),  # 予約一覧
    path('reservation_detail/', CompReservationDetailView.as_view(), name='reservation_detail'),  # 予約詳細
     path('boCheck/', CheckRegiInfoView.as_view(), name='boCheck'),
    path('boRegist/', CreateAccountView.as_view(), name='boRegist'),#新規登録
    path('boMailSend/',BoMailSendView.as_view(),name='boMailSend'),
     path('boLogin/',BoLoginView.as_view(),name='boLogin'),
]
