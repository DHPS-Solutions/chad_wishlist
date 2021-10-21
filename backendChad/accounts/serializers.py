#from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):

    # define own passwords to change paramaters
    password = serializers.CharField(min_length = 4, max_length = 200, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length = 4, max_length = 200, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'first_name',
            'birthday',
            'password',
            'password2',
        ]

        # define passwords as non readable
        extra_kwargs = {'password': {'write_only': True}, 
                       'password2': {'write_only': True}}


    # check validiy of inputs
    def save(self):
        email = self.validated_data['email']
        account = Account(
            email = email,
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            birthday = self.validated_data['birthday'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # email validity
        num_emails = len(Account.objects.filter(email = email))
        if num_emails > 0:
            raise serializers.ValidationError({'email':'Email already exist'}) 
 
        # password validity
        if not password == password2:
            raise serializers.ValidationError({'password':'Passwords doesn\'t match'}) 
        account.set_password(password)
        
        account.save()

        return account
