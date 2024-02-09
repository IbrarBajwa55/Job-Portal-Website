from rest_framework import serializers
from .models import ApplyJob

class ApplyJobSerializer(serializers.ModelSerializer):
  class Meta:
    model=ApplyJob
    fields="__all__"
    
    def create(self, validated_data):
        
        return ApplyJob.objects.create(**validated_data)