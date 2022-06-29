from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import(
    TokenObtainPairView,TokenRefreshView
)

routers =DefaultRouter()
routers.register('courseview',CourseApiView,basename='courseview')

urlpatterns = [
    path('employee/',views.EmployeeView.as_view()),
    path('employee/<int:pk>',views.EmployeeDetail.as_view()),
    path('userview/',views.UserView.as_view()),
    path('userview/<int:pk>',views.Userdetail.as_view()),
    # path('userview/',views.UserView,name="userview"),
    # path('courseapiview/',views.CourseApiView.as_view()),
    # path('courseapiview/<int:pk>',views.CourseApiDetail.as_view()),
    path('',include(routers.urls)),
    path('instructors/',views.InstructorsApiViewset.as_view()),
    path('instructors/<int:pk>',views.InstructorsApiViewsetDetail.as_view(),name='instructors-detail'),
    path('students/',views.StudentsApiViewset.as_view()),
    path('students/<int:pk>',views.StudentsApiViewsetDetail.as_view(),name='students-detail'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

]
