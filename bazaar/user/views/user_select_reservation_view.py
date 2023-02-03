from django.views.generic import TemplateView
from django.contrib.auth.views import(LoginView, LogoutView)
from accounts.forms import LoginForm
from comp.models import Store

from django.shortcuts import render
 
class UserSelectReservationView(LoginView):
     form_class = LoginForm
     template_name = 'user/user_select_reservation.html'
     def get_context_data(self, **kwargs):
          context={}
          st=Store.objects.get(store_id=self.kwargs['pk'])
          context.update({
               'store':st,
          })
          return context