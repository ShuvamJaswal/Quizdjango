from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.decorators import teacher_required
from accounts.forms import *
from .models import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


@never_cache
def home(request):
    if request.user.is_authenticated:
        print(request.user.is_teacher)
        if request.user.is_teacher:
            return redirect('/teacher')
        else:
            return redirect('/student')
    return render(request, 'accounts/home.html')


@method_decorator(never_cache, name='dispatch')
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(
            user=user,)
        login(self.request, user)
        return redirect('/')


@method_decorator(never_cache, name='dispatch')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print(form.data)
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(
            user=user, course=form.cleaned_data.get('course'))
        login(self.request, user)
        return redirect('/')


@never_cache
def signup(request):
    return redirect('/')
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('/')

    if 'teacher' in request.POST:
        form = forms.TeacherSignUpForm()
    else:
        form = forms.StudentSignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})
