from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),#open this if no endpoint entered after /teacher/
    path('quiz/new/', views.addQuiz, name='quiz_new'),
    path('quiz/<str:quiz_id>/addQuestions',views.addQuestion,name='addQuestion')]#str:quiz_id will take string from entered url and save it in quiz_id variable
