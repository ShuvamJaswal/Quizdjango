
from django.http import HttpResponse
from django.shortcuts import render,redirect
from quiz_app_teacher.models import Quiz
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
            return  redirect(f'/teacher/quiz/{quiz.quiz_id}/addQuestions')# HttpResponse("Teacher Home")
    else:
        form =forms.QuizForm()
        return render(request, 'new_quiz.html', {'form': form})
def quiz(request,quiz_id):
    quiz=Quiz.objects.get(quiz_id=quiz_id)
    return render(request,'quiz_t.html',{'quiz_data':quiz,'questions':quiz.questions.all(),'results':quiz.results.all()})
def addQuestion(request,quiz_id):
    quiz=Quiz.objects.get(quiz_id=quiz_id)
    if request.method == "POST":
        form = forms.AddQuestionForm(request.POST) #create a QuizFOrm object using data from request.post
        if form.is_valid():
            question = form.save(commit=False)
            question.question_number=len(quiz.questions.all())+1
            question.save()
            quiz.questions.add(question)
            form=forms.AddQuestionForm()
            #return redirect(request.META['HTTP_REFERER'])
            #return HttpResponse("<script>window.location.href = window.location.href;</script>")
            #return HttpResponse("<script>window.location.reload(false);</script>")
            #return redirect(request.META['HTTP_REFERER'])
            #different return for both form buttons
            return redirect('addQuestion',quiz_id) if "Add Another Question" in request.POST else HttpResponse("Saved")
            #return render(request, 'add_question.html', {'form':  forms.AddQuestionForm(),'questions':quiz.questions.all()}) if "Add Another Question" in request.POST else HttpResponse("Saved")
    else:
        form=forms.AddQuestionForm()
        return render(request, 'add_question.html', {'form': form,'questions':quiz.questions.all()})