from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, uname, password, **extrafields):
        if not uname:
            raise ValueError(_("Username Must Be Set"))
        user = self.model(uname=uname, **extrafields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, uname, password, **extrafields):
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_staff', True)
        return self.create_user(uname, password, **extrafields)