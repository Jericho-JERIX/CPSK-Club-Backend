from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Account, Guild 
from rest_framework import status
from django.forms.models import model_to_dict

@api_view(['GET'])
def core_authentication(request,account_id:int,guild_id:int):
    try:
        account = Account.objects.get(discord_id=account_id)
        guild = Guild.objects.get(guild_id=guild_id)

        print(account,guild)

        return Response({'account':model_to_dict(account),'guild':model_to_dict(guild)},status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)