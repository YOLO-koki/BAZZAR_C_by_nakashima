from django.views.generic import UpdateView
from accounts.models import CustomUser
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.mixins import LoginRequiredMixin

class UserAccountUpdateView(LoginRequiredMixin,UpdateView):
    model=CustomUser
    fields = ['username','mail','phone']
    template_name='user/user_account_update.html'
    

    def get_object(self):
        return CustomUser.objects.get(userid=self.request.user) # or request.POST
    def get_success_url(self):
        return reverse_lazy("accounts:mypage")