from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)

class CourseApi(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=10)
    discount=models.FloatField(max_length=10)
    duration=models.CharField(max_length=50)
    authorName=models.CharField(max_length=50)


class Instructors(models.Model): 
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    instructor=models.ForeignKey(Instructors,on_delete=models.CASCADE,related_name='students')
