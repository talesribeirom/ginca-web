from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from users.forms import User_Creation_Form
from scoremanager.models import Score
from users.models import User
from scoremanager.models import User_has_score


class User_Admin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    add_form = User_Creation_Form

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'date_of_birth', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('date_of_birth', 'sex')}),
        ('Permissões', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'sex', 'password1', 'password2')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Score)
admin.site.register(User_has_score)
admin.site.register(User, User_Admin)

admin.site.unregister(Group)
