
from rest_framework.response import Response

from rest_framework import generics
from apps.company.company_details.models import Company
from apps.job.post_job.models import PostJob

from .serializers import CompanyJobsSerializer

class JobsInCompanyView(generics.ListAPIView):
    serializer_class = CompanyJobsSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return PostJob.objects.filter(company_id=company_id)
       
        
