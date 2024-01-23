from rest_framework import serializers
from apps.post_job.models import PostJob

class PostJobSerializer(serializers.ModelSerializer):
  class Meta:
    model=PostJob
    fields="__all__"