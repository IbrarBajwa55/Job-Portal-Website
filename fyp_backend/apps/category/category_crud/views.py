
from rest_framework import viewsets
from .models import Category
from apps.job.post_job.models import PostJob
from .serializers import CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer

# categories/{category_id}/total_jobs/
    @action(detail=True, methods=['GET'])
    def total_jobs(self, request, pk=None):
        try:
            category = self.get_object()
            total_jobs = PostJob.objects.filter(job_category=category).count()
            return Response({'total_jobs': total_jobs})
        except Exception as e:
            print(e)
            return Response({
                'message':'Category might not exists !! Error'
            })
    