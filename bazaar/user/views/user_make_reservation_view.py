from django.views.generic import FormView
from ..forms import ReservationForm

class UserMakeReservationView(FormView):
    template_name: str = "user/user_make_reservation.html"
    form_class=ReservationForm
    success_url = 'top:index'