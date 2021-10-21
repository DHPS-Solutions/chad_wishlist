from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from accounts.models import Account

# show account model in admin page
@admin.register(Account)
class AccountAdmin(ModelAdmin):
    base_model = Account