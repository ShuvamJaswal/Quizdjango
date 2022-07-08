from django import forms

from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz #model to create form from
        fields = ('name',) #model fields which will be shown in form