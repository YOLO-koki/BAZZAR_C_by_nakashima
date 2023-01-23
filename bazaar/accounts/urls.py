from django.urls import path
#from .views import login_views,logout_views
from .views.login_views import LoginViews
from .views.password_reset_views import PasswordReset
from .views.password_reset_send_views import PasswordResetDone
from .views.password_reset_confim_views import PasswordResetConfirm
from .views.password_reset_complete_views import PasswordResetComplete
from .views.Atest_views import TestView
from django.contrib.auth import views as auth_views
from .views.mypage_views import MypageView
from .views.logout_views import LogoutView


app_name ='accounts'

urlpatterns =[
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),#パスワードリセットページ
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),#パスワードリセット用のメールを送信しましたページ
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),#新パスワード入力用ページ
    path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),#パスワード更新完了ページ
    path('test/', TestView.as_view(), name='test'),#テスト用
    path('mypage/',MypageView.as_view(),name='mypage'),

    #テスト用
    # path('', auth_views.LoginView.as_view(template_name='accounts\login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', LoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
      
