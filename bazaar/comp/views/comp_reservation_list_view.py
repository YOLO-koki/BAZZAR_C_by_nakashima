from django.views.generic import TemplateView
from django.views.generic import ListView
from ..models import Reservation
from django.contrib.auth.mixins import LoginRequiredMixin

# class CompReservationListView(TemplateView):
#     template_name: str = 'comp/bo_reservation_list.html'



class CompReservationListView(LoginRequiredMixin,ListView):
    model = Reservation
    context_object_name = "reservation_list"
    template_name: str = 'comp/bo_reservation_list.html'
    # user_store_id = get_store_id()
    # queryset = Reservation.objects.filter(store_id=user_store_id)

    # def get_store_id(request):
    #     user = request.user.store_id
    #     store_id = user.store_id
    #     return store_id

