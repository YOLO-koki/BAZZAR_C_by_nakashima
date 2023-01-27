from django.views.generic import UpdateView
from ..models.store import Store
from ..models.memu import Menu
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured

class CompMenuUpdateView(UpdateView):
    model=Menu
    fields = ['menu_name','size','price','photo1']
    template_name='comp/bo_mymenu_update.html'
    
    def get_object(self):
        id=Store.objects.get(bp_id=self.request.user)
        return Menu.objects.get(store_id=id) # or request.POST
    def get_success_url(self):
        return reverse_lazy("accounts:mypage")