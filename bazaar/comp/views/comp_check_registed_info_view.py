from django.views.generic import TemplateView


# 登録内容確認
class CompCheckRegistedInfoView(TemplateView):
    template_name: str = 'comp/bo_check_registed_info.html'
