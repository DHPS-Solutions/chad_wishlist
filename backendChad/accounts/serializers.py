from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):


    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'password',
        ]

        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(validated_data)