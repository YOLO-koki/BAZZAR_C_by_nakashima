from django.views.generic import TemplateView
from comp.models import Store,Menu
from accounts.models import CustomUser

class CustomSelectView(TemplateView):
    template_name="comp/bo_custom_select.html"
    model = Store,Menu,CustomUser

    def get_context_data(self,**kwargs):
        context = super(CustomSelectView,self).get_context_data(**kwargs)
        customuserid = CustomUser.objects.get(userid = self.request.user.userid)
        registration_store = Store.objects.filter(bp_id_id = customuserid.userid)

        context['registration_store'] = registration_store

        return context
