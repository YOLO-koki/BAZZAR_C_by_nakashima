from accounts.models import CustomUser
from django.views.generic import TemplateView,ListView
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.contrib.auth.mixins import LoginRequiredMixin


class UserInfoView(LoginRequiredMixin,ListView):
    model = CustomUser
    template_name='user/user_info.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['customuser_list'] = CustomUser.objects.filter(userid=self.request.user)
        return context