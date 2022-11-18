from django.db import models

# Create your models here.
class Account(models.Model):
    discord_id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=50)
    is_core = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class Guild(models.Model):
    guild_id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=50)
    role_core_id = models.CharField(max_length=30)