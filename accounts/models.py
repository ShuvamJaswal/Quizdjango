
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    first_name = models.CharField("first name", max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False)

    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(##TODO:probably not needed.
        'quiz_app_teacher.Quiz', blank=True, related_name='students')
    course = models.ForeignKey(
        'quiz_app_teacher.Course', on_delete=models.CASCADE, related_name='course_students')

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
