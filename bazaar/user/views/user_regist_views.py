from django.views.generic import TemplateView
from django.shortcuts import render


class UserRegistView(TemplateView):

    template_name= "user/user_create_account.html"
    
    def movepage(request):
        if request.POST:
             regiInfo = {
           'id': request.POST["id"],
           'psw': request.POST["psw"],
           'name': request.POST["name"],
           'mail': request.POST["mail"],
           'phone': request.POST["phone"],
        }
             return render(request, 'user/user_check_registed_info.html', regiInfo)

