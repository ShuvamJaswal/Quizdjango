from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from quiz_app_teacher.models import Course
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        # help_text='Required',
        required=True,)
    first_name = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', )

        # labels = {'username': 'fd', 'password': 'None', }
        # help_texts = {  # k:"" for k in fields,
        #     'password2': 'df',
        #     'username': None,
        #     'password1': None,
        #     'password2': None,
        # }

    def clean_email(self):  # TODO:https://youtu.be/qFH8AFQYqME?t=215
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            #self.add_error('email', 'msg')
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

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError({'email': "Email exists"})
    #     return self.cleaned_data

    # def save(self):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data.get('email')
    #     user.save()
    #     student = Student.objects.create(
    #         user=user, course=self.cleaned_data.get('course'))
    #     return user


class TeacherSignUpForm(UserForm):
    pass
    # def save(self, =True):
    #     user = super().save(commit=False)
    #     user.is_teacher = True
    #     if commit:
    #         user.save()
    #         teacher = Teacher.objects.create(user=user)
    #     return user

    # class Meta(UserCreationForm.Meta):
    #     model = User

    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_teacher = True
    #     user.save()
    #     teacher = Teacher.objects.create(user=user)
    # return user


'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from quiz_app_teacher.models import Course
from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200, help_text='Required', required=True,)
class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200, help_text='Required', required=True,)
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        # queryset=Course.objects.all(),
        widget=forms.Select,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_email(self):  # TODO:https://youtu.be/qFH8AFQYqME?t=215
        print("Yoo")
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            #self.add_error('email', 'msg')
            raise forms.ValidationError("This Email is already registered")
        return email
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError({'email': "Email exists"})
    #     return self.cleaned_data

    # def save(self):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data.get('email')
    #     user.save()
    #     student = Student.objects.create(
    #         user=user, course=self.cleaned_data.get('course'))
    #     return user


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
'''
