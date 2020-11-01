from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from funcionario.models import Funcionario
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'nome', 'cpf', 'oficina')
    search_fields = ('nome', 'cpf', 'oficina')
    readonly_fields = ('date_joined','oficina')

    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Funcionario, AccountAdmin)