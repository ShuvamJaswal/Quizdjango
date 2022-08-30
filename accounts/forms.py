from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from quiz_app_teacher.models import Course
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        required=True,)
    first_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This Email is already registered")
        return email

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class StudentSignUpForm(UserForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select,
        required=True, help_text="If your Course isn't listed here, Please contact your Teacher."
    )

class TeacherSignUpForm(UserForm):
    pass
