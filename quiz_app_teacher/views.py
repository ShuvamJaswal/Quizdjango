from django.http import HttpResponse
from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return HttpResponse("Teacher Home")

def addQuiz(request):
    print(request)
    if request.method == "POST": #POST is used to send data secretly
        form = forms.QuizForm(request.POST) #create a QuizFOrm object using data from request.post
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            return HttpResponse("Teacher Home")
    else:
        form =forms.QuizForm()
        return render(request, 'new_quiz.html', {'form': form})