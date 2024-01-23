from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    

    def create(self, validate_data):
      user= CustomUser.objects.create_user(email=validate_data['email'],password=validate_data['password'])
      return user