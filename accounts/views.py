from django.shortcuts import render,redirect
from django.views.generic import CreateView
from accounts.decorators import teacher_required
from accounts.forms import *
from .models import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
  
def home(request):
    if request.user.is_authenticated:
        print(request.user.is_teacher)
        if request.user.is_teacher:
            return redirect('/teacher')
        else:
            return redirect('/student')
    return render(request, 'accounts/home.html')
    
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def signup(request):
    return redirect('/')
    print(request.POST)
    if request.user.is_authenticated:
        return redirect('/')
    
    if 'teacher' in request.POST:
        form=forms.TeacherSignUpForm()
    else:
        form =forms.StudentSignUpForm()
    
    return render(request,'accounts/signup.html', {'form': form})