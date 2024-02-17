from rest_framework.response import Response
from .models import PostJob 
from .serializers import PostJobSerializer
from rest_framework.views import APIView

from rest_framework import status

class PostJobView(APIView):
  def post(self, request, format=None):
    serializer = PostJobSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Job Posted Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
  