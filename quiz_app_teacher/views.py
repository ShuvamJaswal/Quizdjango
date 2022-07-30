from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import *
from django.http import HttpResponseForbidden
from quiz_app_teacher.models import Course, Question, Quiz
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# from quiz_app_teacher.models import Quiz
from . import forms
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.contrib import messages


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class TeacherHome(ListView):
    model = Quiz
   # TODO: ordering = ('', )
    context_object_name = 'myQuizzes'
    template_name = 'teacher/home.html'

    def get_queryset(self):
        queryset = self.request.user.teacher.quizzes.all()
        return queryset


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class newQuiz(CreateView):
    model = Quiz
    #template_name = '/accounts/signup.html'
    template_name = 'teacher/new_quiz.html'
    fields = ['name', 'course', ]

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.author = self.request.user.teacher
        quiz.save()
        # HttpResponse("Teacher Home")
        return redirect(f'/teacher/quiz/{quiz.quiz_id}/addQuestions')


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CourseView(CreateView):
    model = Course
    template_name = 'teacher/course.html'
    fields = ['name', 'year']

    def get_context_data(self, **kwargs):
        kwargs['course_list'] = self.model.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Course added successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get(key='next', default=reverse('teacher:course'))
        # reverse used to get url by giving url name to it which was defined in urls.py

    # def get_success_url(self):
    #     print(self.request.path)

    #     print(self.request.META.get('HTTP_REFERER'))
    #     return redirect(self.request.META.get('HTTP_REFERER'))
    #     return reverse('course',)

    def get_absolute_url(): pass


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
def addQuiz(request):
    print(request)
    if request.method == "POST":  # POST is used to send data secretly
        # create a QuizFOrm object using data from request.post
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            # HttpResponse("Teacher Home")
            return redirect(f'/teacher/quiz/{quiz.quiz_id}/addQuestions')
    else:
        form = forms.QuizForm()
        return render(request, 'new_quiz.html', {'form': form})


@method_decorator(never_cache, name='dispatch')
@method_decorator(quiz_was_created_by_loggedin_user, name='dispatch')
class quiz(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'teacher/quiz_t.html'

    def get_context_data(self, **kwargs):

        kwargs['questions'] = self.get_object().questions.all()
        kwargs['results'] = self.get_object().results.all()
        kwargs['quiz_id'] = self.kwargs.get('quiz_id')
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        'get object will search object from this LIst<>'
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.teacher.quizzes.all()

    def get_object(self):

        return Quiz.objects.get(quiz_id=self.kwargs.get('quiz_id'))


# def quiz(request, quiz_id):
#     quiz = Quiz.objects.get(quiz_id=quiz_id)
#     return render(request, 'quiz_t.html', {'quiz_data': quiz, 'questions': quiz.questions.all(), 'results': quiz.results.all()})
@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
@method_decorator(quiz_was_created_by_loggedin_user, name='dispatch')
class addQuestion(UpdateView):
    model = Question
    template_name = 'teacher/add_question.html'
    fields = ['question', 'A', 'B', 'C', 'D', 'answer', ]

    def get(self, request, *args, **kwargs):
        if self.quiz_obj.results.all():
            return HttpResponseForbidden("You cannot edit a quiz which is attempted by a student.")
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)
    # will be called when view is made( using this in place of init bcz init doesn't have kwargs(data sent by url))

    def dispatch(self, *args, **kwargs):
        self.quiz_obj = get_object_or_404(Quiz, quiz_id=self.kwargs.get(
            'quiz_id'), author=self.request.user.teacher)
        return super(addQuestion, self).dispatch(*args, **kwargs)

    def get_quiz_object(self):
        # print(self.kwargs)

        quiz = get_object_or_404(Quiz, quiz_id=self.kwargs.get(
            'quiz_id'), author=self.request.user.teacher)
        return get_object_or_404(Quiz, quiz_id=self.kwargs.get(
            'quiz_id'), author=self.request.user.teacher)

    def get_object(self, queryset=None):

        return self.model.objects.filter(question_number=self.kwargs.get('question_number'), quiz=self.quiz_obj).first()
        # get_object_or_404(Question, question_number=self.kwargs.get('pk'))
        # return super(addQuestion, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        # Quiz.objects.get(quiz_id=self.kwargs.get('quiz_id'))
        # kwargs['questions'] = self.get_object().questions.all()
        # kwargs['results'] = self.get_object().results.all()
        kwargs['quiz_name'] = self.quiz_obj.name
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if(self.kwargs.get('question_number')):
            self.object = form.save()
            return redirect(f"/teacher/quiz/{self.kwargs.get('quiz_id')}/")
        print(self.object)
        question = form.save(commit=False)
        question.question_number = len(
            self.quiz_obj.questions.all())+1
        question.quiz = self.quiz_obj
        question.save()
        # HttpResponse("Teacher Home")
        return redirect(f"/teacher/quiz/{self.kwargs.get('quiz_id')}/")


# def addQuestion(request, quiz_id):
#     quiz = Quiz.objects.get(quiz_id=quiz_id)
#     if request.method == "POST":
#         # create a QuizFOrm object using data from request.post
#         form = forms.AddQuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.question_number = len(quiz.questions.all())+1
#             question.save()
#             quiz.questions.add(question)
#             form = forms.AddQuestionForm()
#             # return redirect(request.META['HTTP_REFERER'])
#             # return HttpResponse("<script>window.location.href = window.location.href;</script>")
#             # return HttpResponse("<script>window.location.reload(false);</script>")
#             # return redirect(request.META['HTTP_REFERER'])
#             # different return for both form buttons
#             return redirect('addQuestion', quiz_id) if "Add Another Question" in request.POST else HttpResponse("Saved")
#             # return render(request, 'add_question.html', {'form':  forms.AddQuestionForm(),'questions':quiz.questions.all()}) if "Add Another Question" in request.POST else HttpResponse("Saved")
#     else:
#         form = forms.AddQuestionForm()
#         return render(request, 'add_question.html', {'form': form, 'questions': quiz.questions.all()})
