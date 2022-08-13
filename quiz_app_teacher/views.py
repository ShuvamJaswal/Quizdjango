from dataclasses import field
from genericpath import exists
import imp
from tkinter.ttk import Style
from django import forms
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from accounts.decorators import *
from django.http import HttpResponseForbidden
from quiz_app_teacher.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
# call these decorators in CBV on a specific function in this case 'dispatch'


@method_decorator([login_required, teacher_required], name='dispatch')
# so that browser doesn't stores web page n reloads it from server(even when pressing back button.)
@method_decorator(never_cache, name='dispatch')
class TeacherHome(ListView):
    model = Quiz
    # variable used to access sent data in templates
    context_object_name = 'myQuizzes'
    template_name = 'teacher/home.html'

    def get_queryset(self):
        queryset = self.request.user.teacher.quizzes.all().order_by('created_date')
        return queryset


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class newQuiz(CreateView):
    model = Quiz
    template_name = 'teacher/new_quiz.html'
    fields = ['name', 'course', ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['course'].queryset = Course.objects.order_by('name')
        return form

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.author = self.request.user.teacher
        quiz.save()
        messages.add_message(self.request, messages.SUCCESS,
                             "Quiz has been created Successfully. Now you can add questions.")
        return redirect(f'/teacher/quiz/{quiz.quiz_id}/addQuestions')


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CourseView(CreateView):
    model = Course
    template_name = 'teacher/course.html'
    fields = ['name', 'year']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = self.model.objects.all().order_by('name',
                                                                   'year')
        return context

    def form_valid(self, form):

        if Course.objects.filter(name=form.cleaned_data.get('name').upper(), year=form.cleaned_data.get('year')).exists():
            messages.success(self.request, 'Course already exists')
            return redirect(self.get_success_url())
        course = form.save(commit=False)
        course.name = form.cleaned_data.get('name').upper()
        course.save()
        messages.add_message(self.request, messages.SUCCESS,
                             'Course added successfully.')
        return redirect(self.get_success_url())
        # TODO do from here

    def get_success_url(self):
        # get value of return keyword if it exists
        return self.request.GET.get(key='next', default=reverse('teacher:course'))
        # reverse used to get url by giving url name to it which was defined in urls.py

    # def get_absolute_url(): pass


@method_decorator(never_cache, name='dispatch')
@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(quiz_was_created_by_loggedin_user, name='dispatch')
class quiz(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'teacher/quiz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = self.get_object().questions.all()
        context['results'] = self.get_object(
        ).results.all().order_by('-points')
        context['quiz_id'] = self.kwargs.get('quiz_id')
        context['quiz'] = self.get_object()
        return context

    def get_queryset(self):
        return self.request.teacher.quizzes.all()

    def get_object(self):
        return Quiz.objects.get(quiz_id=self.kwargs.get('quiz_id'))


@method_decorator([login_required, teacher_required], name='dispatch')
@method_decorator(never_cache, name='dispatch')
@method_decorator(quiz_was_created_by_loggedin_user, name='dispatch')
class addQuestion(UpdateView):
    model = Question
    template_name = 'teacher/add_question.html'
    fields = ['question', 'A', 'B', 'C', 'D', 'answer', ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['answer'].widget = forms.RadioSelect(
            choices=ANSWER_CHOICES)
        form.helper = FormHelper()
        form.helper.attrs = {"novalidate": ''}
        form.helper.form_class = 'form-horizontal'
        form.helper.label_class = "control-label  col-12 col-md-3"
        form.helper.field_class = "col"
        # form.helper['answer'].wrap(InlineRadios, style="margin-left: 10px;")
        form.helper.layout = Layout('question', 'A', 'B', 'C', 'D',
                                    InlineRadios('answer',
                                                 style="margin-left: 10px;")
                                    )
        # form.helper[:].wrap(Field, css_class='pull-right',
        #                     style="max-width:80%; ")
        # form.helper['answer'].wrap(Field, 'answer', css_class="hhhhh")
        # .wrap(Div, style="margin-left: 10px;", css_class='djdj')
        # form.helper.layout = Layout( InlineRadios('answer'))
        # form.helper.layout = Layout(Fieldset('A', 'B',
        #                                      Div(
        #                                           # I need to set size for every field wrapped in a div
        #                                           Div('tipo_logradouro',
        #                                               css_class="col-md-6"),
        #                                           Div('logradouro',
        #                                               css_class='col-md-6'),
        #                                           css_class='row'
        #                                      ),))
        # form.helper.layout = Layout(
        #     Div(Field('A', css_class="col-sm-1"),
        #         css_class="form-group",)
        # )
        # form.helper.layout = Layout(
        #     Row(
        #         Column('question', css_class='form-group col-md-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Field('A', css_class="black-fields"),

        #     Div('B', css_class="form-group row")
        # )
        form.helper.add_input(
            Submit('submit', 'Done', css_class='btn-primary'))
        form.helper.form_method = 'POST'
        return form

    def get(self, request, *args, **kwargs):
        if self.quiz_obj.results.all():
            return HttpResponseForbidden("You cannot edit a quiz which is attempted by a student.")
        return super().get(request, *args, **kwargs)

    # will be called when view is made( using this in place of init bcz init doesn't have kwargs(data sent by url))
    def dispatch(self, *args, **kwargs):
        self.quiz_obj = get_object_or_404(Quiz, quiz_id=self.kwargs.get(
            'quiz_id'), author=self.request.user.teacher)
        return super(addQuestion, self).dispatch(*args, **kwargs)

    def get_quiz_object(self):
        return self.quiz_obj

    def get_object(self, queryset=None):
        return self.quiz_obj.questions.filter(question_number=self.kwargs.get('question_number'),).first()
        # will give question object if in updateView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz_name'] = self.quiz_obj.name
        return context

    def form_valid(self, form):
        # if(self.kwargs.get('question_number')):
        #     self.object = form.save()
        #     return redirect(f"/teacher/quiz/{self.kwargs.get('quiz_id')}/")
        # question = form.save(commit=False)
        # question.question_number = len(
        #     self.quiz_obj.questions.all())+1
        question = form.save(commit=False)
        question.quiz = self.quiz_obj
        question.save()
        # HttpResponse("Teacher Home")
        return redirect(f"/teacher/quiz/{self.kwargs.get('quiz_id')}/")


class ResultView(DetailView):
    model = Result
    context_object_name = 'result'
    template_name = 'teacher/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_data'] = eval(self.get_object().get_answer())

        context['questions'] = Quiz.objects.get(
            quiz_id=self.kwargs.get('quiz_id')).questions.all()
        context['quiz_id'] = self.kwargs.get('quiz_id')
        return context

    def get_object(self):
        print(self.kwargs.get('result_id'))
        return Result.objects.get(id=self.kwargs.get('result_id'))
