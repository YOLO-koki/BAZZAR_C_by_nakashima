from django.urls import path
from .views import CoStoreDetailView

app_name = 'bazaar'
urlpatterns = [
    path('detail',CoStoreDetailView.as_view(),name="detail")
]
