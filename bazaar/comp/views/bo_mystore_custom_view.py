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
    success_url = reverse_lazy('top:index')

    # def get_form_kwargs(self):
    #     kwgs = super().get_form_kwargs()
    #     kwgs["user"] = self.request.user
    #     return kwgs
    # def form_send(request):
    #     if request.method=="POST":
    #          bp=Store(bp_id=request.user)
    #          form=StoreForm(request.post,
    #          instance=bp)
    #          if form.is_valid():
    #             form.save()
    #             return redirect('top:index')


    def form_valid(self, form):
        hoge=form.save(commit=False)  # 保存処理など
        hoge.bp_id=self.request.user
        hoge.save()
        return redirect('mypage/<str:userid>')
    # def get_form_kwargs(self):
    #     kwgs = super().get_form_kwargs()
    #     kwgs["bp_id"] = self.request.post['userid']
    #     return kwgs
    # def form_valid(self, form):
    #     return render(request=self.request,template_name="comp/bo_check_registed_info.html",context={'form':form})