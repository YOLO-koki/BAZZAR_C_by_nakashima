from django.views.generic import TemplateView
from comp.models import Store

class CustomSelectView(TemplateView):
    template_name="comp/bo_custom_select.html"
    model = Store

    def get_object(self):
        id=Store.objects.get(bp_id_id=self.request.user)
        store = Store.objects.filter(store_id=id).exists
        return store