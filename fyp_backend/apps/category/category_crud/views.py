from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
# from rest_framework.decorators import action
# from rest_framework.response import Response
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    
    #companies/{companyId}/emplyees
    # @action(detail=True,methods=['get'])
    # def employees(self,request,pk=None):   
    #     try:                
    #         company=Company.objects.get(pk=pk)
    #         emps=Employee.objects.filter(company=company)
    #         emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
    #         return Response(emps_serializer.data)
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'message':'Company might not exists !! Error'
    #         })

