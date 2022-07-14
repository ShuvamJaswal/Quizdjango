from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
class StudentSignUpForm(UserCreationForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user,course=self.cleaned_data.get('course'))
        return user

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            teacher = Teacher.objects.create(user=user)
        return user



    # class Meta(UserCreationForm.Meta):
    #     model = User

    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_teacher = True
    #     user.save()
    #     teacher = Teacher.objects.create(user=user)
        # return user