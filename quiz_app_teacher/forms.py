from operator import mod
from django import forms

from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz #model to create form from
        fields = ('name',) #model fields which will be shown in form

# class AddQuestionForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AddQuestionForm, self).__init__(*args, **kwargs)
#         self.fields['answer'] = forms.ChoiceField(choices=models.ANSWER_CHOICES, widget=forms.RadioSelect(),)

#     class Meta:
#         model=models.Question
#         answer = forms.ChoiceField(choices=models.ANSWER_CHOICES, widget=forms.RadioSelect())
#         fields=('questionTitle','option1','option2','option3','option4',)

class AddQuestionForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AddQuestionForm, self).__init__(*args, **kwargs)
    #     self.fields['answer'] = forms.ChoiceField(choices=models.ANSWER_CHOICES, widget=forms.RadioSelect(),)
    
    class Meta:
        
        model=models.Question
        exclude = ('question_number',)

        #widgets={'answer':forms.RadioSelect(attrs={'class': 'form-check-inline','size':'400'})}
        # widgets={'answer': forms.IntegerField(required=True, label="Mobile No",
        #                            widget=forms.NumberInput(attrs={'type': 'number',
        #                                                            'id': 'org_mobile_no',
        #                                                            'name': 'org_mobile_no',
        #                                                            'value': "",
        #                                                            'class': 'form-control'}))}
        #answer = forms.CharField(label='a', widget=forms.RadioSelect())
        #widgets={'answer':forms.CharField(label='a', widget=forms.RadioSelect())}
        fields=('question','A','B','C','D','answer',)
        #,"""choices=models.ANSWER_CHOICES,"""