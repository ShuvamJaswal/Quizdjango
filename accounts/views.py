from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import *
from .models import *
from django.contrib.auth import login, logout
import django.contrib.auth.views as auth_views
# Create your views here.
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from django.contrib import messages


@never_cache
def home(request):
    if request.user.is_authenticated:
        print(request.user.is_teacher)
        if request.user.is_teacher:
            return redirect('/teacher/')
        elif request.user.is_student:
            return redirect('/student/')
        else:
            return redirect('/admin')
    return render(request, 'accounts/home.html')


class UserLogin(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return super().get_default_redirect_url()


@method_decorator(never_cache, name='dispatch')
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'Teacher'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(
            user=user,)
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS,
                             "Your account has been created")
        return redirect('/')


@method_decorator(never_cache, name='dispatch')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'Student'
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['course'].queryset = Course.objects.order_by('name')
        return form

    def form_valid(self, form):
        print(form.data)
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(
            user=user, course=form.cleaned_data.get('course'))
        login(self.request, user)

        messages.add_message(self.request, messages.SUCCESS,
                             "Your account has been created")
        return redirect('/')


@never_cache
def signup(request):
    return redirect('/')
