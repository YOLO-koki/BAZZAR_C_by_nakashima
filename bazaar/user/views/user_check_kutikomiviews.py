from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from comp.models.kuchikomi import Kuchikomi
from accounts.models import CustomUser
from comp.models.store import Store
from ..forms import KutikomiForm
from django .shortcuts import redirect
# from ..forms import RegisterForm

# from django.core.exceptions import ValidationError

class UserCheckKutikomiView(TemplateView):
    template_name = "user/user_review_check.html"
    model = Kuchikomi,CustomUser,Store
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userReviewPerfect')

    def form_valid(self, form):
        kuchikomi_content=form.save(commit=False)
        store_id = Store.objects.get(store_id=self.kwargs['pk'])
        kuchikomi_content.store_id=store_id
        return redirect('user:userReviewPerfect')
    