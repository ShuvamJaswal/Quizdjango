from django.contrib.auth.models import AbstractUser
from django.db import models
from quiz_app_teacher.models import *
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    Year=models.IntegerField()
    def __str__(self):
        return self.name

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz)
    course  = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='class_students')
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz,)
    def __str__(self):
        return self.user.username

