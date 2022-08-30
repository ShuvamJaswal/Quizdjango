import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from quiz_app_teacher.models import Result, Quiz
from django.db.models import Count
from accounts.decorators import student_required
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.


@method_decorator([login_required, student_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class StudentHome(ListView):
    model = Quiz
    context_object_name = 'myQuizzes'
    template_name = 'student/home.html'

    def get_queryset(self):
        current_student = self.request.user.student
        current_student_quizzes = current_student.course.quizzes.annotate(
            question_count=Count('questions')).filter(question_count__gt=0)  # quizzes having more than 0 questions.

        not_taken = current_student_quizzes.exclude(
            id__in=[i.quiz.id for i in current_student.my_results.all()]).order_by('-created_date')

        taken = current_student_quizzes.filter(
            id__in=[i.quiz.id for i in current_student.my_results.all()]).order_by('-created_date')

        queryset = {'not_taken': not_taken, 
                    'taken': taken}

        return queryset


@method_decorator(never_cache, name='dispatch')
class ResultView(DetailView):
    model = Result
    context_object_name = 'result'
    template_name = 'student/result.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['answer_data'] = eval(self.get_object().get_answer())

        context['questions'] = Quiz.objects.get(
            quiz_id=self.kwargs.get('quiz_id')).questions.all()
        context['quiz_id'] = self.kwargs.get('quiz_id')
        return context

    def get_object(self):
        return Result.objects.get(id=self.kwargs.get('result_id'))


@never_cache
@login_required
@student_required
def quiz(request, quiz_id):
    current_quiz = Quiz.objects.get(quiz_id=quiz_id)
    if Result.objects.filter(student=request.user.student, quiz=current_quiz).exists():
        result = Result.objects.filter(
            student=request.user.student, quiz=current_quiz)[0]
        return redirect(f'resultview/{result.id}')
    else:
        if request.method == "POST":
            questions = current_quiz.questions.all()
            correct = []
            incorrect = []
            unanswered = []
            answer_data = {}
            for question in questions:
                ques = 'Question ' + str(question.question_number)
                if ques in request.POST:
                    answer_data[ques] = request.POST[ques]
                unanswered.append(question) if ques not in request.POST else correct.append(
                    question) if question.answer == request.POST[ques] else incorrect.append(question)
              
            points = len(correct)
            answer_data = json.dumps(answer_data)
            result = Result.objects.create(
                student=request.user.student, points=points, quiz=current_quiz, answer_data=answer_data)
            return redirect(request.META.get('HTTP_REFERER'))

        else:
            questions = current_quiz.questions.all()
            context = {'quiz': current_quiz,
                       'questions': questions
                       }
            return render(request, 'student/quiz.html', context)
