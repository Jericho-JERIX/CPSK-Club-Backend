from django.contrib import admin
from .models import Account,Guild

class AccountAdmin(admin.ModelAdmin):
    list_display = ['discord_id','name','is_core','is_active']
    search_fields = ['name']
    list_filter = ['is_core','is_active']

class GuildAdmin(admin.ModelAdmin):
    list_display = ['guild_id','name','role_core_id']
    search_fields = ['name']

admin.site.register(Account,AccountAdmin)
admin.site.register(Guild,GuildAdmin)