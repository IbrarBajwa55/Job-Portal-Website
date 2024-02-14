from rest_framework import serializers
from .models import PostJob
from apps.category.category_crud.serializers import CategorySerializer

class PostJobSerializer(serializers.ModelSerializer):
  job_category=CategorySerializer()
  class Meta:
    model=PostJob
    fields="__all__"
    