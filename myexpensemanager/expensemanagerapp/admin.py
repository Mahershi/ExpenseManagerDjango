from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('uname', 'password',)}),
        (_('Personal Info'), {'fields': ('name', 'email',)}),
        (_('Permission'), {'fields': ('is_superuser',)}),
        (_('Data'), {'fields': ('image_url', 'fcm_token', 'date_joined',)})
    )

    list_display = ('email', 'name', 'uname',)
    list_filter = ('uname',)
    filter_horizontal = ()
    search_fields = ('email', 'name', 'uname')
    ordering = ('name',)



