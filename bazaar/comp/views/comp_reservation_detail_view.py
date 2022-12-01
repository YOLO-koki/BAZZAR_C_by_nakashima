from django.views.generic import TemplateView

class CompReservationDetailView(TemplateView):
    template_name: str = 'comp/bo_reservation_detail.html'