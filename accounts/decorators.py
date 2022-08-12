from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from quiz_app_teacher.models import Quiz
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
def teacher_required(
    function=None,
):
    actual_decorator = user_passes_test(
        lambda u: u.is_teacher,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def student_required(
    function=None,
):
    actual_decorator = user_passes_test(
        lambda u: u.is_student,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def quiz_was_created_by_loggedin_user(function=None):
    def wrap(request, *args, **kwargs):
        quiz = Quiz.objects.get(quiz_id=kwargs['quiz_id'])
        if quiz.author == request.user.teacher:
            return function(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR,
                                 "You aren't allowed to visit that page")
            return redirect('/')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
