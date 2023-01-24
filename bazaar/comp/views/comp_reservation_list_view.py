from django.views.generic import TemplateView
from django.views.generic import ListView
from ..models import Reservation,Store,Menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class CompReservationListView(LoginRequiredMixin,ListView):
    model = Reservation
    #context_object_name = "reservation_list"
    template_name: str = 'comp/bo_reservation_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompReservationListView, self).get_context_data(**kwargs)
        #予約情報を取得
        store_id = Store.objects.get(bp_id_id = self.request.user.userid)
        reservation = Reservation.objects.filter(store_id_id = store_id)
        context['reservation'] = reservation
        #メニュー名を取得
        menu1_id = reservation.values('menu1_id')
        menu1_name = Menu.objects.filter(id__in = menu1_id)
        context['menu1_name'] = menu1_name
        
        return context

    # def get_queryset(self):
    #     reservations = Reservation.objects.filter(store_id_id = store_id)
    #     return reservations
    


    # user_store_id = get_store_id()
    # queryset = Reservation.objects.filter(store_id=user_store_id)

    def get_store_id(request):
        user = request.user.store_id
        store_id = user.store_id
        return store_id

