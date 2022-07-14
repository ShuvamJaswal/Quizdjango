from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),#open this if no endpoint entered after /student/
    path('quiz/<str:quiz_id>/',views.quiz,name='quiz')
]
