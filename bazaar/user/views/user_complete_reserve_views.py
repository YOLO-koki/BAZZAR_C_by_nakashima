from django.views.generic import FormView,CreateView,TemplateView,ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..forms import ReservationForm
from comp.models import Store,Reservation
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

from django.core.exceptions import ValidationError


class UserCheckReserveView(FormView):
     template_name="user/user_check_reserve.html"
     form_class = ReservationForm
     def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        r_store=self.kwargs.get('pk')
        store=Store.objects.get(store_id=r_store)
        ctx['store']=store
        ctx['reservation_name']=self.request.POST('reservation_name')
        ctx['reservation_day']=self.request.POST('reservation_day')
        ctx['reservation_hour']=self.request.POST('reservation_hour')
        return render(request=self.request,template_name="user/user_check_reserve.html",context={'form':ctx})



class UserCompleteReserveView(TemplateView):
    template_name="user/user_complete_reserve.html"