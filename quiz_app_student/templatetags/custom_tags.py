from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):

    return dictionary.get("Question "+str(key))


@register.filter
def is_answer_correct(user_answer, correct_answer):
    if not user_answer:
        return
    elif user_answer == correct_answer:
        return
    return "bg-danger"


@register.filter
def assign_border_based_on_answer(user_answer, correct_answer):
    if not user_answer:
        return "border-warning"
    elif user_answer == correct_answer:
        return "border-success"
    return "border-danger"
