from wkhtmltopdf.views import PDFTemplateView
from ..models import Reservation
from django.views.generic import ListView
from .comp_reservation_list_view import CompReservationListView

class HTMLtoPDF(PDFTemplateView):
    filename = 'reservationList.pdf'
    template_name = 'bo_reservation_list.html'
