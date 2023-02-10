from django.views.generic import FormView
from ..forms import ReservationForm
from django.shortcuts import render
from comp.models import Store
import datetime
from django.shortcuts import redirect
class UserMakeReservationView(FormView):
    template_name: str = "user/user_make_reservation.html"
    form_class=ReservationForm
    success_url = 'top:index'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_hour=self.kwargs.get('hour')
        date=self.kwargs.get('dt')   
        r_dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        r_store=self.kwargs.get('pk')
        store=Store.objects.get(store_id=r_store)
        context['hour']=r_hour
        context['date']=r_dt.date
        context['store']=store
        context['empty']=self.request.GET['param']
        return context
    
    def form_valid(self, form):
         res = form.save(commit=False)
         res.store_id=Store.objects.get(store_id=self.kwargs.get('pk'))
         res.reservation_day=self.kwargs.get('dt')
         res.reservation_hour=self.kwargs.get('hour')
         res.save()
         return render(request=self.request,template_name="user/user_complete_reserve.html",context={'form':res})
