from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get(self, request):
        return Response(Account.objects.all())
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        serializer.save()
        return Response(serializer.data, status = HTTP_201_CREATED)