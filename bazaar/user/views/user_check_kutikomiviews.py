from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView
from django.urls import reverse_lazy
from accounts.models import CustomUser
from comp.models import Store,Kuchikomi
from ..forms import KutikomiForm
from django .shortcuts import redirect
# from ..forms import RegisterForm

# from django.core.exceptions import ValidationError

class UserCheckKutikomiView(CreateView):
    template_name = "user/user_review_check.html"
    model = Kuchikomi,CustomUser,Store
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userReviewPerfect')

    def form_valid(self, form):
        form.save()
        return redirect('user:userReviewPerfect')