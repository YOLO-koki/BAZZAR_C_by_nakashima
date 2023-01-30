from django.views.generic import FormView
from ..forms import ReservationForm
from django.shortcuts import render
from comp.models import Store
class UserMakeReservationView(FormView):
    template_name: str = "user/user_make_reservation.html"
    form_class=ReservationForm
    success_url = 'top:index'
    def form_valid(self,form):
        hoge=form.save(commit=False)
        hoge.store_id=Store.objects.get(store_id=self.kwargs['pk'])
        hoge.save()
        return render(request=self.request,template_name="user/user_complete_reserve.html",context={'store':hoge})