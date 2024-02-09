from django.shortcuts import render
from apps.job.post_job.models import PostJob
from .serializers import GetAllJobsSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class Job_List(ListAPIView):
    queryset=PostJob.objects.all()
    serializer_class=GetAllJobsSerializer