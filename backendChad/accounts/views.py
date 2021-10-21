from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    # GET. respond with list of accounts
    def list(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    

    # POST. create a new account
    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'New account registered.'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['birthday'] = account.birthday

        else:
            data = serializer.errors
        
        return Response(data)
        