from django.shortcuts import render
from .serializers import StudentSeriazer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passby='Teacher1')
    queryset = Student.objects.all()        
    serializer_class = StudentSeriazer
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']