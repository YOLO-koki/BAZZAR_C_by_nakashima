
from django.views.generic import TemplateView
from django.views.generic import ListView
from comp.models import Reservation,Store,Menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from  datetime import date,datetime,timedelta
# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class UserReservationView(LoginRequiredMixin,ListView):
    model = Reservation
    template_name: str = 'user/user_reservation.html'

    def get_context_data(self, **kwargs):
        context = super(UserReservationView, self).get_context_data(**kwargs)
        #現在の日付を取得
        dt_now = datetime.now()

        reservation = Reservation.objects.filter(reservation_day__gte=dt_now)
        reservation = reservation.filter(user_id_id = self.request.user.userid).order_by('reservation_day')
        
        store_id = reservation.values_list('store_id_id')
        store_name = Store.objects.filter(store_id__in = store_id)
        # store_name = Store.objects.select_related('store_id').get(store_id = store_id)
        #reservation = reservation.annotate()
        context['reservation'] = reservation
        # context['reservation'] = store_name
        context['store_name'] = store_name
        
        return context
        

