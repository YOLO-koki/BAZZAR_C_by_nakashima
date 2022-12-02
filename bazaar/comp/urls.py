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
    CompReservationDetailView,
    CompLogoutView,
)
app_name = 'comp'
urlpatterns = [
    path('mypage/<str:userid>', CompMypageView.as_view(), name='mypage'),  # マイページ
    path('login/', CompLoginView.as_view(), name='login'),  # ログイン機能
    path('logout/', CompLogoutView.as_view(), name='logout'),  # ログアウト機能
    path('signup/', CompSignupView.as_view(), name='signup'),  # 新規登録機能
    path('check_registed_info/', CompCheckRegistedInfoView.as_view(), name='check_registed_info'),  # 登録内容確認
    path('send_url/', CompSendURLView.as_view(), name='send_url'),  # URL送信案内
    path('reset_password/', CompResetPasswordView.as_view(), name='reset_password'),  # パスワードリセットURL送信
    path('update_password/', CompUpdatePasswordView.as_view(), name='update_password'),  # パスワード更新
    path('reservation_list/', CompReservationListView.as_view(), name='reservation_list'),  # 予約一覧
    path('reservation_detail/', CompReservationDetailView.as_view(), name='reservation_detail'),  # 予約詳細
]
