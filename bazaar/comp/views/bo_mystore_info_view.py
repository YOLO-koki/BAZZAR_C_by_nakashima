from ..models.store import Store
from accounts.models import CustomUser
from django.views.generic import TemplateView,ListView
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from ..models.memu import Menu


class CompStoreInfoView(ListView):

    template_name='comp/bo_mystore_info.html'
    model=Store
    
    def get_queryset(self):
        stores=Store.objects.filter(bp_id=self.request.user)
        return stores
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['customuser_list'] = CustomUser.objects.filter(userid=self.request.user)
        store=Store.objects.get(bp_id=self.request.user)
        context['menu_list'] = Menu.objects.filter(store_id=store)
        return context
    
    


    # @cached_property
    # def get_data(self):
    #     myId=self.request.user
    #     myInfo=Store.objects.get(bp_id=myId)
    #     return myInfo
