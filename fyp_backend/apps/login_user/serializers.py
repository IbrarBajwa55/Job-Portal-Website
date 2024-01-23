from rest_framework import serializers
from apps.register_user.models import CustomUser

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = CustomUser
    fields = ['email', 'password']
