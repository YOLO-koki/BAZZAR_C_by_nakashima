from .models import CustomUser

class CompBackend:
    def authenticate(self, userid=None, password=None):
        user = self.get_user(self, userid)

        auth_result = False

        if user:
            if password == CustomUser.objects.get(pk=userid).password:
                print(password)
                print(CustomUser.objects.get(pk=userid).password)
                auth_result = True
            else:
                auth_result = False

        if auth_result:
            try:
                user = CustomUser.objects.get(userid=userid)
            except CustomUser.DoesNotExist:
                user = None
            return user
        else:
            return None
    
    def get_user(self, userid):
        try:
            return CustomUser.objects.get(pk=userid)
        except CustomUser.DoesNotExist:
            return None