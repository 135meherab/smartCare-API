from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username', 'first_name', 'last_name', 'email']

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'erroe': 'email already exists'})
        elif password != password2:
            raise serializers.ValidationError({'error': "password doesn't match"})
        else:
            account = User(username=username, email= email, first_name=first_name, last_name=last_name)
            account.set_password(password)
            account.is_active = False
            account.save()
            return account

class UserloginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    