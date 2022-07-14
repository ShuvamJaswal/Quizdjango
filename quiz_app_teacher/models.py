from cProfile import label
from django.utils import timezone
from django.db import models
from django.conf import settings
from accounts import models
# Create your models here.
ANSWER_CHOICES = (
   ('A', 'A'),
   ('B', 'B'),
   ('C','C'),
   ('D','D'),
)
class Quiz(models.Model):
 # many2many for having a list of questions inside quiz
    #attempted_by=models.ManyToManyField(settings.AUTH_USER_MODEL,)
    #result=models.ManyToManyField()
    #Quiz.objects.get(quiz_id="fgvf-1749").questions.all()
    #https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
    #https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
    name=models.CharField(max_length=250)
    quiz_id=models.CharField(max_length=300,)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(models.User, on_delete=models.CASCADE,related_name='quizzes')
    subject = models.ForeignKey(models.Course, on_delete=models.CASCADE, related_name='quizzes')

    def save(self, *args, **kwargs):
        #override default save method to do something before saving object of model
        if not self.quiz_id:
            self.quiz_id = self.name+"-"+self.created_date.strftime("%M%S")  #TODO:Edit this 
        super(Quiz, self).save(*args, **kwargs)
    def __str__(self):
        return self.name 

class result(models.Model):
    #quiz=models.OneToOneField(Quiz,on_delete=models.CASCADE)
    student=models.ForeignKey(models.User, on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    points=models.IntegerField()
    def __str__(self):
        return  f"Student name: { str(self.student)} Points:{ str(self.points)}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    #quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question=models.CharField(max_length=300,)
    A = models.CharField(max_length=200,)
    B = models.CharField(max_length=200,)
    C = models.CharField(max_length=200,)
    D = models.CharField(max_length=200,)
    answer = models.CharField(max_length=200,choices=ANSWER_CHOICES,default='A')
    question_number=models.IntegerField()
    def __str__(self):
        return self.question
