from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import User, Expense, Cluster, Category
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('uname', 'password',)}),
        (_('Personal Info'), {'fields': ('name', 'email',)}),
        (_('Permission'), {'fields': ('is_superuser',)}),
        (_('Data'), {'fields': ('image_url', 'fcm_token', 'date_joined',)})
    )

    add_fieldsets = (
        (None, {'fields': ('uname', 'password1', 'password2')}),
        (_('Personal Info'), {'fields': ('name', 'email',)}),
        (_('Permission'), {'fields': ('is_superuser',)}),
        (_('Data'), {'fields': ('image_url', 'fcm_token', 'date_joined',)})
    )

    list_display = ('id', 'email', 'name', 'uname',)
    list_filter = ('is_superuser', )
    filter_horizontal = ()
    search_fields = ('email', 'name', 'uname')
    ordering = ('name', 'id')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'amount', 'category', 'user_id', 'cluster', 'expense_date', 'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('name', 'amount', 'category', 'user_id', 'cluster', 'expense_date', 'is_active', 'created_date',)}),
    )

    list_display = ('id', 'name', 'amount', 'user_id', 'cluster', 'expense_date')
    list_filter = ('category', 'cluster', 'user_id')
    filter_horizontal = ()
    search_fields = ('name', 'id', 'user_id')
    ordering = ('name', 'id', 'amount')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'image_url')}),
    )

    add_fieldsets = (
        (None, {'fields': ('name', 'image_url')}),
    )

    list_display = ('id', 'name', 'image_url')
    list_filter = ()
    filter_horizontal = ()
    search_fields = ('name', 'id',)
    ordering = ('name', 'id',)

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'expenses', 'user_id', 'created_date', )}),
    )

    add_fieldsets = (
        (None, {'fields': ('name', 'expenses', 'user_id', 'created_date', )}),
    )

    list_display = ('id', 'name', 'expenses', 'user_id')
    list_filter = ('user_id',)
    filter_horizontal = ()
    search_fields = ('name', 'id', 'user_id')
    ordering = ('name', 'id',)