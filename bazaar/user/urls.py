from django.urls import path
from .views.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
