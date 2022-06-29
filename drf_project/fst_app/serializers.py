from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = '__all__'

class CourseApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseApi
        fields = '__all__'


class StudentsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'        

class InstructorsSerializers(serializers.HyperlinkedModelSerializer):
    students=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='students-detail')
    class Meta:
        model = Instructors
        fields = '__all__' 