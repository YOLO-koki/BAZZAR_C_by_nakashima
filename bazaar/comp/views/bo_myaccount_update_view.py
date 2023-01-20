from django.views.generic import UpdateView
from accounts.models import CustomUser
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured

class CompAccountUpdateView(UpdateView):
    model=CustomUser
    fields = ['username','mail','phone','age','adress']
    template_name='comp/bo_myaccount_update.html'
    

    def get_object(self):
        return CustomUser.objects.get(userid=self.request.user) # or request.POST
    def get_success_url(self):
        return reverse_lazy("comp:mypage", kwargs={"pk": self.request.user})