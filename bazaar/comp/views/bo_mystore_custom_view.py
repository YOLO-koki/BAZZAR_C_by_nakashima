from django.views.generic import TemplateView
from django.views.generic import FormView,View
from django.urls import reverse_lazy
from ..forms import StoreForm
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render
from comp.models import Store

# def CompMyStoreCustomView(request):
    # if request.method == 'POST':
    #     form = StoreForm(request.POST)
    #     if form.is_valid():
    #         test = form.save(commit=False)
    #         test.bp_id = request.user.userid
    #         test.save()
    #         return redirect('comp:bostorecustom')
    # else:
    #         form = StoreForm()
class CompMyStoreCustomView(FormView):
    template_name = 'comp/bo_mystore_custom.html'
    form_class=StoreForm
  
    def get_success_url(self):
        return reverse_lazy("accounts:mypage")
    
    def form_valid(self, form):
        hoge=form.save(commit=False)  # 保存処理など
        hoge.bp_id=self.request.user
        fuga=hoge.store_id
        hoge.save()
        return render(request=self.request,template_name="accounts/mypage.html",context={'fuga':fuga})