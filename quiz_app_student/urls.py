from django.urls import path

from . import views
app_name = 'student'
urlpatterns = [
    path('', views.StudentHome.as_view(), name='home'),
    path('quiz/<str:quiz_id>/', views.quiz, name='quiz'),
    path('quiz/<str:quiz_id>/resultview/<int:result_id>',
         views.ResultView.as_view(), name='result_view'),
]
