from email import message
# from django.shortcuts import render,HttpResponse
# from django.http import JsonResponse
from .models import *
from .serializers import *
from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import ViewSet , ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.authentication import BasicAuthentication ,TokenAuthentication
# Create your views here.


'''-***********************************-'''

'''using api view function'''
# @api_view(['GET','POST'])
# def EmployeeView(request):
#     if request.method == 'GET':    
#         employee = Employee.objects.all()
#         serializer=EmployeeSerializers(employee,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=EmployeeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data )
#         else:
#             return Response(serializer.errors) 


# @api_view (['GET','DELETE','PUT'])
# def EmployeeDetail(request,pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method =="DELETE":
#         employee.delete()
#         return HttpResponse(status=204)
#     elif request.method == "GET":
#         serializer=EmployeeSerializers(employee)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer=EmployeeSerializers(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data )
#         else:
#             return Response(serializer.errors) 

'''-***********************************-'''
# @api_view(['GET','POST'])
# def UserView(request):
#     if request.method =="GET":
#         user = User.objects.all()
#         serializer=UserSerializers(user,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer=UserSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 

'''-***********************************-'''

'''-***********************************-'''
'''using generic class view'''
class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers    


'''-***********************************-'''


'''using mixin class'''
class UserView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class Userdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def get(self, request,pk):
        return self.retrieve(request, pk)
    def put(self, request,pk):
        return self.update(request, pk)
    def delete(self, request,pk):
        return self.destroy(request, pk) 

'''-***********************************-'''


# @api_view(['GET','POST'])
# def CourseApiView(request):
#     if request.method == 'GET':
#         courseapi = CourseApi.objects.all()
#         serializer = CourseApiSerializers(courseapi, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CourseApiSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:    
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
'''-************************************-'''

 # @api_view (['GET','DELETE','PUT'])
# def CourseApiDetail(request,pk):
#     try:
#         courseapi = CourseApi.objects.get(pk=pk)
#     except CourseApi.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method =="DELETE":
#         courseapi.delete()
#         return HttpResponse(status=204)
#     elif request.method == "GET":
#         serializer=CourseApiSerializers(courseapi)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer=CourseApiSerializers(courseapi,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data )
#         else:
#             return Response(serializer.errors)
'''-***********************************-'''

'''using APIView class'''

# class CourseApiView(APIView):
#     def get(self, request):
#         courseapi = CourseApi.objects.all()
#         serializer = CourseApiSerializers(courseapi, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CourseApiSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CourseApiDetail(APIView):
   
#     def get_object(self, pk):
#         try:
#             return CourseApi.objects.get(pk=pk)
#         except CourseApi.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         courseapi = self.get_object(pk)
#         serializer =CourseApiSerializers(courseapi)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         courseapi = self.get_object(pk)
#         serializer = CourseApiSerializers(courseapi, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         courseapi = self.get_object(pk)
#         courseapi.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
'''-***********************************-'''
class CourseApiView(ModelViewSet):
    queryset = CourseApi.objects.all()
    serializer_class = CourseApiSerializers


'''-***********************************-'''

class InstructorsApiViewset(generics.ListCreateAPIView):
    queryset = Instructors.objects.all()
    serializer_class = InstructorsSerializers
class InstructorsApiViewsetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructors.objects.all()
    serializer_class = InstructorsSerializers 

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if request.method == "GET":
            return True
        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False        



class StudentsApiViewset(generics.ListCreateAPIView):
 
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers    
class StudentsApiViewsetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers    