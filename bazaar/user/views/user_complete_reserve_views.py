from django.views.generic import TemplateView,ListView
class UserCompleteReserveView(TemplateView):
    template_name: str = "user/user_complete_reserve.html"