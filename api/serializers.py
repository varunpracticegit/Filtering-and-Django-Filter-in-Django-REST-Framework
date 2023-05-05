from rest_framework import serializers
from .models import Student

class StudentSeriazer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city', 'passby']