from django.urls import path
from .views import account

urlpatterns = [
    path('accounts/<int:account_id>/guilds/<int:guild_id>',account.core_authentication)    
]
