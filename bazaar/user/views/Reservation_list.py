from django.views.generic import TemplateView
from django.views.generic import ListView
from comp.models import Reservation,Store,Menu
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class UserReservationlistView(LoginRequiredMixin,ListView):
    model = Reservation
    #context_object_name = "reservation_list"
    template_name: str = 'user/user_reservation_list.html'

    # def get(self, request, **kwargs):
    #     store_name = Store.objects.filter(user_id_id = self.request.user.userid)
    #     ctx = {
    #         'store_name': store_name, 
    #     }
    #     return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        context = super(UserReservationlistView, self).get_context_data(**kwargs)

        reservation = Reservation.objects.filter(user_id_id = self.request.user.userid)
        
        store_id = reservation.values_list('store_id_id')
        store_name = Store.objects.filter(store_id__in = store_id)
        context['reservation'] = reservation
        context['store_name'] = store_name
        
        return context
        
    # def get_queryset(self):
    #     reservation_list = Reservation.objects.filter(user_id_id = self.request.user).order_by('-time')
    #     return reservation_list
    



    # user_store_id = get_store_id()
    # queryset = Reservation.objects.filter(store_id=user_store_id)

    # def get_store_id(request):
    #     user = request.user.store_id
    #     store_id = user.store_id
    #     return store_id

