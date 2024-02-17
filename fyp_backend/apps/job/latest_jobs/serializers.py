from rest_framework import serializers
from apps.job.post_job.models import PostJob

class LatestJobsSerializer(serializers.ModelSerializer):
  class Meta:
    model=PostJob
    fields="__all__"
    