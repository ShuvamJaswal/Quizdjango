from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),#open this if no endpoint entered after /teacher/
    path('quiz/new/', views.addQuiz, name='quiz_new'),]
