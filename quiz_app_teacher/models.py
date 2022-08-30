import json
from django.utils import timezone
from django.db import models
# Create your models here.
ANSWER_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)
COURSE_YEAR_CHOICES = (
    (1, '1st'),
    (2, '2nd'),
    (3, '3rd'),
    (4, '4th'),
)


class Course(models.Model):
    # class Meta:
    #     ordering = ('name',)
    name = models.CharField(max_length=30)
    year = models.PositiveIntegerField(choices=COURSE_YEAR_CHOICES, default=1,)

    def __str__(self):
        return f'{self.name} ({dict(COURSE_YEAR_CHOICES).get(self.year)} Year)'


class Quiz(models.Model):
    
    name = models.CharField(max_length=250)
    quiz_id = models.CharField(max_length=300,)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        'accounts.Teacher', on_delete=models.CASCADE, related_name='quizzes')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='quizzes',)

    def save(self, *args, **kwargs):
        if not self.quiz_id:
            self.quiz_id = f"{self.name.replace(' ','-')}-{self.created_date.strftime('%M%S')}"
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} By: {self.author} at {self.created_date.strftime('%H:%M, %d/%m/%Y')}"

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering=['-created_date']


class Result(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE,
                                related_name='my_results')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='results')
    points = models.IntegerField(default=0)
    answer_data = models.TextField(default='{}')
    max_points = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(default=timezone.now)
    def get_answer(self):
        return eval(json.dumps(self.answer_data))
    def save(self, *args, **kwargs):
        if not self.max_points:
            self.max_points = len(self.quiz.questions.all())
        super(Result, self).save(*args, **kwargs)
    def __str__(self):
        return f"Student name: { str(self.student)} Max Points:{str(self.max_points)} Obtained Points:{str(self.points)}"


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=300,)
    A = models.CharField(max_length=200,)
    B = models.CharField(max_length=200,)
    C = models.CharField(max_length=200,)
    D = models.CharField(max_length=200,)
    answer = models.CharField(
        max_length=200, choices=ANSWER_CHOICES, default='A')
    question_number = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.question_number:
            self.question_number = len(self.quiz.questions.all()) + 1
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.question_number}. {self.question}"
