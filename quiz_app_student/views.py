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
   # TODO: ordering = ('', )
    context_object_name = 'myQuizzes'
    template_name = 'student/home.html'

    def get_queryset(self):
        # taken_quizzes = self.request.user.student.my_results.all()
        # Quiz.objects.filter(
        #     quiz_id__in=self.request.user.student.my_results.quiz_id)
        data = self.request.user.student.course.quizzes.all().order_by('-created_date')
        queryset = {'not_taken': data.exclude(id__in=self.request.user.student.my_results.all()),  # id__in results.objects.all # result.filter(student=request.user.stdudent)


                    'taken': data.filter(id__in=self.request.user.student.my_results.all())}

        # self.request.user.student.course.quizzes.all().annotate(
        #   taken=Quiz.objects.all())
        # TODO:refactor code queryset written twice
        current_student = self.request.user.student

        current_student_quizzies = current_student.course.quizzes.annotate(
            question_count=Count('questions')).filter(question_count__gt=0)  # quizzes having more than 0 questions.

        not_taken = current_student_quizzies.exclude(
            id__in=[i.quiz.id for i in current_student.my_results.all()]).order_by('-created_date')  # Result.objects.filter(student=current_student)
        # Result.objects.filter(student=current_student)

        taken = current_student_quizzies.filter(
            id__in=[i.quiz.id for i in current_student.my_results.all()]).order_by('-created_date')

        b = Result.objects.filter(student=self.request.user.student)
        c = Quiz.objects.filter(course=self.request.user.student.course).exclude(id__in=[i.quiz.id for i in Result.objects.filter(
            student=self.request.user.student)])
        queryset = {'not_taken': not_taken,  # id__in results.objects.all # result.filter(student=request.user.stdudent)
                    'taken': taken}

        return queryset


@method_decorator(never_cache, name='dispatch')
class ResultView(DetailView):
    model = Result
    context_object_name = 'result'
    template_name = 'student/result.html'

    def get_context_data(self, **kwargs):

        # kwargs['questions'] = self.get_object().questions.all()
        context = super().get_context_data(**kwargs)
        context['answer_data'] = eval(self.get_object().get_answer())

        context['questions'] = Quiz.objects.get(
            quiz_id=self.kwargs.get('quiz_id')).questions.all()
        context['quiz_id'] = self.kwargs.get('quiz_id')
        return context

    def get_object(self):
        return Result.objects.get(id=self.kwargs.get('result_id'))


@never_cache
# TODO:use in other places too prevent restroing form data if user presses back button
@login_required
@student_required
def quiz(request, quiz_id):
    current_quiz = Quiz.objects.get(quiz_id=quiz_id)
    if Result.objects.filter(student=request.user.student, quiz=current_quiz).exists():
        result = Result.objects.filter(
            student=request.user.student, quiz=current_quiz)[0]
        return redirect(f'resultview/{result.id}')
        return redirect('/')
        return HttpResponse('already attempted '+str(result))
    else:
        if request.method == "POST":
            questions = current_quiz.questions.all()
            correct = []
            incorrect = []
            unanswered = []
            answer_data = {}
            for question in questions:
                a = 'Question ' + str(question.question_number)
                if a in request.POST:
                    answer_data[a] = request.POST[a]
                # if a not in request.POST:
                #     print(1)
                #     unanswered.append(question)
                # else:
                #     if question.answer == request.POST[a]:
                #         correct.append(question)
                #         print(2)
                #     else:
                #         print(3)
                #         incorrect.append(question)
                #         print("inc"+str(incorrect))

                # print(question.answer)
                # print(request.POST[a] if a in request.POST else '')
                # print(request.POST[a] == question.answer)
                # print(a)
                # print(question.answer)
                # print(request.POST[a] if a in request.POST else '')
                
                unanswered.append(question) if a not in request.POST else correct.append(
                    question) if question.answer == request.POST[a] else incorrect.append(question)
                # print('u' if a not in request.POST else 'c' if question.answer ==
                #       request.POST[a] else 'i')
                # request.POST[question]
            print(
                f'correct {correct}\n incorrect {incorrect}\n unanswered {unanswered}')
            points = len(correct)
            answer_data = json.dumps(answer_data)
            r = Result.objects.create(  # max_points=len(questions),
                student=request.user.student, points=points, quiz=current_quiz, answer_data=answer_data)
            print(request.POST)
            return redirect(request.META.get('HTTP_REFERER'))
            return redirect('/student')

        else:
            questions = current_quiz.questions.all()
            context = {'quiz': current_quiz,
                       'questions': questions
                       }
            return render(request, 'student/quiz.html', context)
