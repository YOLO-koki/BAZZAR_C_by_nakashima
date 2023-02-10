from django.views.generic import UpdateView
from ..models.store import Store
from ..models.memu import Menu
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured

class CompMenuUpdateView(UpdateView):
    model=Menu
    fields = ['menu_name1','size1','price1','photo1','about1','menu_name2','size2','price2','photo2','about2','menu_name3','size3','price3','photo3','about3','menu_name4','size4','price4','photo4','about4']
    template_name='comp/bo_mymenu_update.html'
    
    def get_object(self):
        id=Store.objects.get(bp_id=self.request.user)
        return Menu.objects.get(store_id=id) # or request.POST
    def get_success_url(self):
        return reverse_lazy("accounts:mypage")