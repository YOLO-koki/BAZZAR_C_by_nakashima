from comp.forms import LoginCustomUserForm
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.backends import CompBackend
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

# ログイン機能


class CompLoginView(View):
    def get(self, *args, **kwargs):
        template_name: str = 'comp/bo_login.html'
        form = LoginCustomUserForm()

        return render(request=self.request, template_name=template_name, context={'form': form})

    def post(self, *args, **kwargs):
        userid = self.request.POST['userid']
        password = self.request.POST['password']
        data = [userid, password]
        form = LoginCustomUserForm(self.request, data=data)
        user = CompBackend.authenticate(self=CompBackend, userid=userid, password=password)
        username = get_user_model().objects.get(pk=userid).username

        if user:
            login(request=self.request, user=user, backend='accounts.backends.CompBackend')
            # return render(request=self.request, template_name=template_name)
            return redirect(to=reverse('comp:mypage', args=[userid]))
            
        else:
            form = LoginCustomUserForm(self.request.POST)
            return render(request=self.request, template_name='comp/bo_login.html', context={'form': form, 'error': 'パスワードかユーザーIDが間違っています。'})
    
