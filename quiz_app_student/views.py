from django.http import HttpResponse
from django.shortcuts import render

from quiz_app_teacher.models import result, Quiz

# Create your views here.
def index(request):
    return render(request,"home.html")

def quiz(request,quiz_id):
    if request.method == "POST":
        r=result.objects.create(student=request.user,points=80)
        Quiz.objects.get(quiz_id=quiz_id).results.add(r)
        print("fhdhsfgdsjhfgsduyhfgsdhug")
        print(request.POST)
    questions=Quiz.objects.get(quiz_id=quiz_id).questions.all()
    context = {
            'questions':questions
        }
    return render(request,'quiz.html',context)