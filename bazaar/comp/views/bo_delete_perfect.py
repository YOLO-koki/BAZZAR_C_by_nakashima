from django.shortcuts import render
from ..models import Store
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import send_email

#ログインしていることが条件
class DeletePerfectView(LoginRequiredMixin, TemplateView):
    template_name = "comp/bo_delete_perfect.html"

    def __init__(self): #hiddenから受け取り
        self.params = {
        'delete_store_id':'',
        }

    def post(self,request):
        delete_store_id = request.POST['delete_store_id']
        self.params['delete_store_id'] = delete_store_id
        abc = self.params

        sent_email(abc) #メール送信

        return render(request,'comp/bo_delete_perfect.html',abc)

def sent_email(abc):#メール送信
    send_email(abc)