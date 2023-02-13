from wkhtmltopdf.views import PDFTemplateView
from django.shortcuts import redirect
from ..models import Reservation, Store
from django.views.generic import ListView
from .comp_reservation_list_view import CompReservationListView
from datetime import datetime, timedelta

class HTMLtoPDF(PDFTemplateView):
    filename = 'reservationList.pdf'
    template_name = 'bo_reservation_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #現在の日付を取得
        dt_now = datetime.now()
        #2日後の日付を取得
        dt_2day = dt_now + timedelta(days=2)
        #StoreテーブルからログインしているユーザーのストアIDを取得
        store_id = Store.objects.get(bp_id_id = self.request.user.userid)#
        reservation = Reservation.objects.filter(reservation_day__range=[dt_now, dt_2day])
        reservation = reservation.filter(store_id_id = store_id).order_by('reservation_day')
        #reservation = reservation.filter(reservation.values(reservation_day__range=[dt_now, dt_2day]))
        context['reservation'] = reservation
        return context