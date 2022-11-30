from django.urls import path
from .views.login_views import LoginViews

app_name ='accounts'

urlpatterns =[
    path('', LoginViews.as_view(), name='login'),
    #path('logout/', views.Logout.as_view(), name='logout'),
]
      
