from django.views.generic import FormView
from comp.models import Store,Menu
from accounts.models import CustomUser
from ..forms import DeleteForm
from django.urls import reverse_lazy

class DeleteForm(FormView):
    template_name="comp/bo_delete.html"
    form_class = DeleteForm
    success_url = reverse_lazy('comp:deleteperfect')