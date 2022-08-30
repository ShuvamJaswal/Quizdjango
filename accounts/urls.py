from django.urls import include, path
from django.http import HttpResponse
import django.contrib.auth.views as auth_views
import django.contrib.auth.urls
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'),),
    path('accounts/login/', views.UserLogin.as_view(
        template_name='accounts/login.html',), name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/signup/student/',
         views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/',
         views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
