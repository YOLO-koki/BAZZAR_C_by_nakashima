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

app_name = 'user'
urlpatterns = [
    path('', UserIndexView.as_view(),name = 'index'),#トップページ
    path('usermypage/', UserMypageView.as_view(),name = 'mypage'),#トップページ
    path('userCheck/', CheckRegiInfoView.as_view(), name='userCheck'),
    path('userRegist/', CreateAccountView.as_view(), name='userRegist'),#新規登録
    path('userComplete/', UserCompleteView.as_view(), name='userComplete'),
    path('userLogin/',UserLoginView.as_view(),name='userLogin'),
    path('userMailSend/',UserMailSendView.as_view(),name='userMailSend'),
    path('userKutikomi/',UserKutikomiView.as_view(),name='userKutikomi'),#口コミ
    path('userCheckKutikomi/',UserCheckKutikomiView.as_view(),name='userCheckKutikomi'),#口コミ確認
    path('userReviewPerfect/',UserReviewPerfectView.as_view(),name='userReviewPerfect'),#口コミ送信完了

    ]