from django.urls import path
from . import views
app_name = 'teacher'  # adding app_name so that we can use namespaces in url while reversing eg while giving link in html we can use 'teacher:quiz' so that it doesn't go to student/quiz
urlpatterns = [
    # open this if no endpoint entered after /teacher/
     path('', views.TeacherHome.as_view(), name='home'),
     path('course', views.CourseView.as_view(), name='course'),
     path('quiz/new/', views.newQuiz.as_view(), name='quiz_new'),
     # str:quiz_id will take string from entered url and save it in quiz_id variable
     path('quiz/<str:quiz_id>/', views.quiz.as_view(), name='quiz'),
     path('quiz/<str:quiz_id>/addQuestions',
         views.addQuestion.as_view(), name='addQuestion'),
     path('quiz/<str:quiz_id>/addQuestions/<int:question_number>',
         views.addQuestion.as_view(), name='updateQuestion'),
     path('quiz/<str:quiz_id>/resultview/<int:result_id>',
         views.ResultView.as_view(), name='result_view'),
    path('quiz/<str:quiz_id>/resultview/<int:result_id>',
         views.ResultView.as_view(), name='result_view'),
         
]
