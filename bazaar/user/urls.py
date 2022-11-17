from django.urls import path
from .views.user_check_infoviews import UserCheckView
from .views.user_regist_views import UserRegistView
from .views.user_complete_registerviews import UserCompleteView
from .views.user_loginviews import UserLoginView
from .views.user_mail_sendviews import UserMailSendView
from .views.indexview import IndexView
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('userCheck/', UserCheckView.as_view(), name='userCheck'),
    path('userRegist/', UserRegistView.as_view(), name='userRegist'),
    path('userComplete/', UserCompleteView.as_view(), name='userComplete'),
    path('userLogin/',UserLoginView.as_view(),name='userLogin'),
    path('userMailSend/',UserMailSendView.as_view(),name='userMailSend')

]
