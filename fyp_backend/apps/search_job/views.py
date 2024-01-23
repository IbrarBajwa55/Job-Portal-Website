from django.shortcuts import render
from apps.post_job.models import PostJob
from .serializers import PostJobSerializer
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters


# Create your views here.
class SearchJoblist(ListAPIView):
    queryset=PostJob.objects.all()
    serializer_class= PostJobSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('job_title','job_location')