from django.shortcuts import render

from apps.job.post_job.models import PostJob
from .serializers import GetAllJobsSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class Latest_Jobs(ListAPIView):
    queryset=PostJob.objects.all()[::-1][:8]
    serializer_class=GetAllJobsSerializer
