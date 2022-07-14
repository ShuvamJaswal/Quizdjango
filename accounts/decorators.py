from django.contrib.auth.decorators import user_passes_test
def teacher_required(
    function=None, 
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_teacher,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
