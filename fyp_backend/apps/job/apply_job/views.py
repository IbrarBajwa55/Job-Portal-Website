from rest_framework.response import Response
from .models import ApplyJob
from .serializers import ApplyJobSerializer
from rest_framework.views import APIView
from rest_framework import status

class ApplyJobView(APIView):
  def post(self, request, format=None):
    serializer = ApplyJobSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Apply Job Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
  
