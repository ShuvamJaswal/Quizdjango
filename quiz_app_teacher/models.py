from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=250)
    quizId=models.CharField(max_length=300,)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        #override default save method to do something before saving object of model
        if not self.quizId:
            self.quizId = self.name+str(self.created_date)  #TODO:Edit this 
        super(Quiz, self).save(*args, **kwargs)
    def __str__(self):
        return self.name 
class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionTitle=models.CharField(max_length=300,)
    option1 = models.CharField(max_length=200,)
    option2 = models.CharField(max_length=200,)
    option3 = models.CharField(max_length=200,)
    option4 = models.CharField(max_length=200,)
    answer = models.CharField(max_length=200,)
    
    def __str__(self):
        return self.questionTitle
