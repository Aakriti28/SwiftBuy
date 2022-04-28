from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .forms import RegisterUserForm
from .models import Users

# Register your models here.

class MyUserAdmin(UserAdmin):
    add_form = RegisterUserForm
    # form = UserChangeForm
    model = Users
    list_display = ('email', 'name', 'phone', 'address', 'shipping_address', 'referral_token', 'wallet_amount', 'role')
    list_filter = ('email', 'name', 'phone', 'address', 'shipping_address', 'referral_token', 'wallet_amount', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'address', 'shipping_address', 'referral_token', 'wallet_amount', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone', 'address', 'shipping_address', 'referral_token', 'wallet_amount', 'role')}
        ),
    )
    filter_horizontal = ()
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Users, MyUserAdmin)