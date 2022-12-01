from django.views.generic import TemplateView

class CompReservationListView(TemplateView):
    template_name: str = 'comp/bo_reservation_list.html'