from django.urls import path
from .views import (
    CompLoginView,
    CompLogoutView,
    CompSignupView,
    CompCheckRegistedInfoView,
    CompSendURLView,
    CompResetPasswordView,
    CompUpdatePasswordView,
    CompMypageView,
    CompReservationListView,
    CompReservationDetailView,
    CheckRegiInfoView,
    CreateAccountView,
    BoMailSendView,
    BoLoginView,
    CompMyStoreCustomView,
    CompStoreInfoView,
    CompStoreUpdateView,
    CompMenuCustomView,
    CustomSelectView,
    CompAccountUpdateView,
    CompMenuUpdateView,
    CompReservationListAllView,
    CustomPerfectView,
    DeleteForm,
    DeletePerfectView,
    HTMLtoPDF,
)
# from .views.bo_check_infoviews import CheckRegiInfoView
# from .views.bo_regist_views import CreateAccountView
# from .views.bo_mail_sendviews import BoMailSendView
# from .views.bo_loginviews import BoLoginView

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'comp'
urlpatterns = [
    #path('mypage/<str:userid>/', CompMypageView.as_view(), name='mypage'),  # マイページ
    # path('mypage/', CompMypageView.as_view(), name='mypage'),  # マイページ
    # path('login/', CompLoginView.as_view(), name='login'),  # ログイン機能
    # path('logout/', CompLogoutView.as_view(), name='logout'),  # ログアウト機能
    # path('signup/', CompSignupView.as_view(), name='signup'),  # 新規登録機能
    # path('check_registed_info/', CompCheckRegistedInfoView.as_view(), name='check_registed_info'),  # 登録内容確認
    # path('send_url/', CompSendURLView.as_view(), name='send_url'),  # URL送信案内
    # path('reset_password/', CompResetPasswordView.as_view(), name='reset_password'),  # パスワードリセットURL送信
    # path('update_password/', CompUpdatePasswordView.as_view(), name='update_password'),  # パスワード更新

    path('boCheck/', CheckRegiInfoView.as_view(), name='boCheck'),
    path('boMailSend/',BoMailSendView.as_view(),name='boMailSend'),

    #  path('boLogin/',BoLoginView.as_view(),name='boLogin'),
    #path('mypage/<str:pk>/', CompMypageView.as_view(), name='mypage'),

    path('reservation_list/', CompReservationListView.as_view(), name='reservation_list'),  # 予約一覧(２日後)
    path('change_to_pdf/', HTMLtoPDF.as_view(), name='change_to_pdf'),  # 予約一覧(２日後)
    path('reservation_list_all/',CompReservationListAllView.as_view(),name="reservation_list_all"),#予約一覧ページ(全部)
    path('reservation_detail/', CompReservationDetailView.as_view(), name='reservation_detail'),  # 予約詳細
    path('boStoreCustom/',CompMyStoreCustomView.as_view(),name='boStoreCustom'),
    path('boStoreInfo/<str:userid>/',CompStoreInfoView.as_view(),name='boStoreInfo'),
    path('boStoreUpdate/<str:userid>/',CompStoreUpdateView.as_view(),name='boStoreUpdate'),
    path('boAccountUpdate/<str:userid>/',CompAccountUpdateView.as_view(),name='boAccountUpdate'),
    path('boMenuUpdate/<str:userid>/',CompMenuUpdateView.as_view(),name='boMenuUpdate'),
    path('menucustom/',CompMenuCustomView.as_view(),name='menucustom'),
    path('customselect/<str:userid>',CustomSelectView.as_view(),name='customselect'),
    path('boRegist/', CreateAccountView.as_view(), name='boRegist'),#新規登録
    path('customperfect/',CustomPerfectView.as_view(), name = "customperfect"),
    path('deleterequest/',DeleteForm.as_view(),name="delete"),
    path('deleteperfect/',DeletePerfectView.as_view(),name = "deleteperfect"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

