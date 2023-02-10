from django.urls import path
from .views.user_regist_views import CreateAccountView 
from .views.user_check_infoviews import CheckRegiInfoView
from .views import UserCompleteView
from .views import UserLoginView
from .views import UserMailSendView
from .views import UserIndexView
from .views import UserMypageView
from .views import UserKutikomiView
from .views import UserCheckKutikomiView
from .views import UserReviewPerfectView
from .views import UserReservationlistView
from .views import UserReservationView
from .views import UserInfoView
from .views import UserAccountUpdateView
from .views import UserMakeReservationView
from .views import UserSelectReservationView
from .views import UserMakeReservationLoginView
from .views import UserCompleteReserveView,UserCheckReserveView
from django.conf import settings
from django.conf.urls.static import static
from .views import CalenderView

app_name = 'user'
urlpatterns = [
    path('', UserIndexView.as_view(),name = 'index'),#トップページ
    path('usermypage/', UserMypageView.as_view(),name = 'mypage'),#トップページ
    path('userKutikomi/<int:pk>/',UserKutikomiView.as_view(),name='userKutikomi'),#口コミ
    path('userCheckKutikomi/',UserCheckKutikomiView.as_view(),name='userCheckKutikomi'),#口コミ確認
    path('userReviewPerfect/',UserReviewPerfectView.as_view(),name='userReviewPerfect'),#口コミ送信完了
    path('user_info/',UserInfoView.as_view(),name="user_info"),#ユーザー情報ページ
    path('user_accounts_update/<str:userid>/',UserAccountUpdateView.as_view(),name='userAccountUpdate'),#ユーザー情報更新ページ
    path('reservation_list/',UserReservationlistView.as_view(),name="reservation_list"),#予約履歴ページ
    path('reservation/',UserReservationView.as_view(),name="reservation"),#予約確認ページ
    path('userRegist/', CreateAccountView.as_view(), name='userRegist'),#新規登録
    path('userCheck/', CheckRegiInfoView.as_view(), name='userCheck'),
    path('userMailSend/',UserMailSendView.as_view(),name='userMailSend'),
#以下使ってない

    path('userCheck/', CheckRegiInfoView.as_view(), name='userCheck'),
    # path('userComplete/', UserCompleteView.as_view(), name='userComplete'),
    # path('userLogin/',UserLoginView.as_view(),name='userLogin'),
    path('userMailSend/',UserMailSendView.as_view(),name='userMailSend'),
    path('userMakeReservation/<str:pk>/<int:hour>/<str:dt>/',UserMakeReservationView.as_view(),name='userMakeReservation'),
    path('userMakeReservationLogin/<str:pk2>//<int:pk>/<int:hour>/<str:dt>/',UserMakeReservationLoginView.as_view(),name='userMakeReservationLogin'),
    path('loginUserMakeReservation/<int:pk>/',UserMakeReservationLoginView.as_view(),name='loginUserMakeReservation'),
    path('userSelectReservation/<int:pk>/',UserSelectReservationView.as_view(),name='userSelectReservation'),
    path('userCompReservation/<int:pk>/<int:hour>/<str:dt>/',UserCompleteReserveView.as_view(),name='userCompReservation'),
    path('userCalender/<int:pk>/<int:year>/<int:month>/<int:day>/',CalenderView.as_view(),name='userCalender2'),
    path('userCalender/<str:pk2>/<int:pk>/<int:year>/<int:month>/<int:day>/',CalenderView.as_view(),name='userCalender2'),
    path('userCalender/<int:pk>/',CalenderView.as_view(),name='userCalender'),
    path('userCalender/<str:pk2>/<int:pk>/',CalenderView.as_view(),name='userCalender'),
    path('userCheckReservation/<int:pk>/<int:hour>/<str:dt>/',UserCheckReserveView.as_view(),name='userCheckReservation'),
    ]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)