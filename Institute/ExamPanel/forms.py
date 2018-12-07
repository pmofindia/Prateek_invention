from django.forms import ModelForm
from django import forms
from .models import *
from Institute.models import *
from ckeditor_uploader.fields import RichTextUploadingFormField

Ans = [
    ['1', '1'],
    ['2', '2'],
    ['3', '3'],
    ['4', '4'],
]


class CreateExamPackageForm(forms.ModelForm):
    class Meta:
        model = ExamPackage
        exclude = ()
        widgets = {
            'course':forms.Select(attrs={
                                     'class': 'form-control show-tick',
                                          "required": ''
                                     }),
            'name': forms.TextInput(attrs={'placeholder': 'Package Name', "class":"form-control"}),
            'fee': forms.TextInput(attrs={'placeholder': 'Package Name', "value":"0",
                                          "class": "form-control"}),
            'logo': forms.FileInput(attrs={ "class":"form-control" }),
            'syllabus': forms.FileInput(attrs={ "class":"form-control"})
        }


class CreateExamSubPackageForm(forms.ModelForm):
    class Meta:
        model = ExamSubPackage
        exclude = ('course',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Package Name', "class":"form-control"}),
            'syllabus': forms.FileInput(attrs={ "class":"form-control"})
        }


class CreateMainExamForm(forms.ModelForm):
    class Meta:
        model = MainExam
        exclude = ('course',)

        widgets = {
            'instruction':RichTextUploadingFormField(),
           # 'Sub_package':forms.Select(attrs={ 'class': 'form-control show-tick',"required": ''
            #                               }),
            'name': forms.TextInput(attrs={'placeholder': 'Exam Name', "class": "form-control", "required":""}),
            'duration': forms.TextInput(attrs={'placeholder': 'Exam Duration ex. HH:MM',
                            "class":"form-control", "pattern":"([0-1]?[0-9]|2[0-4]):([0-5][0-9])", "required":""}),
            'syllabus': forms.FileInput(attrs={"class": "form-control"})

        }



class MultiChoiseQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestions
        exclude = ('quiz', 'exam', 'practice',

                   'Type2', 'Question', 'Option1', 'Option2', 'Option3', 'Option4',
                   'Answer1', 'Answer2', 'Answer3', 'Answer4', 'marks2', 'minus2',
                   'Type3', 'Que', 'Answer31', 'Answer32', 'marks3', 'minus3',
                   'Type4', 'Ques_tion', 'TrueAns1', 'marks4', 'minus4')

        widgets = {
            'Questions': RichTextUploadingFormField(),
            'Option_1': RichTextUploadingFormField(),
            'Option_2': RichTextUploadingFormField(),
            'Option_3': RichTextUploadingFormField(),
            'Option_4': RichTextUploadingFormField(),

            'TrueAns': forms.Select(attrs={'class': 'form-control show-tick', "required": ''
                                               }),
            'marks1': forms.TextInput(attrs={'placeholder': '+Ve Mark', "class": "form-control"}),
            'minus1': forms.TextInput(attrs={'placeholder': '+Ve Mark', "class": "form-control"}),
            'Type1': forms.CheckboxInput(attrs={'checked': 'checked', 'hidden':""}),

        }



class MultiResponseQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestions
        exclude = ('quiz', 'exam', 'practice',
                   'Type1', 'Questions', 'Option_1',
                   'Option_2', 'Option_3', 'Option_4', 'TrueAns', 'marks1',
                   'minus1',
                   'Type3', 'Que', 'Answer31', 'Answer32', 'marks3', 'minus3',
                   'Type4', 'Ques_tion', 'TrueAns1', 'marks4', 'minus4')

        widgets = {
            'Question': RichTextUploadingFormField(),
            'Option1': RichTextUploadingFormField(),
            'Option2': RichTextUploadingFormField(),
            'Option3': RichTextUploadingFormField(),
            'Option4': RichTextUploadingFormField(),

            'Answer1': forms.CheckboxInput(),
            'Answer2': forms.CheckboxInput(),
            'Answer3': forms.CheckboxInput(),
            'Answer4': forms.CheckboxInput(),

            'marks2': forms.TextInput(attrs={'placeholder': '+Ve Mark', "class": "form-control"}),
            'minus2': forms.TextInput(attrs={'placeholder': '-Ve Mark', "class": "form-control"}),
            'Type2': forms.CheckboxInput(attrs={'checked': 'checked', 'hidden': ""}),


        }


class FillInTheBlankQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestions
        exclude = ('quiz', 'exam', 'practice',
                   'Type1', 'Questions', 'Option_1',
                   'Option_2', 'Option_3', 'Option_4', 'TrueAns', 'marks1',
                   'minus1',
                   'Type2', 'Question', 'Option1', 'Option2', 'Option3', 'Option4',
                   'Answer1', 'Answer2', 'Answer3', 'Answer4', 'marks2', 'minus2',

                   'Type4', 'Ques_tion', 'TrueAns1', 'marks4', 'minus4')

        widgets = {
            'Que': RichTextUploadingFormField(),
            'Answer31': forms.TextInput(attrs={'placeholder': 'Correct Answer', "class": "form-control"}),
            'Answer32': forms.TextInput(attrs={'placeholder': 'Correct Answer (Optional)', "class": "form-control"}),
            'marks3': forms.TextInput(attrs={'placeholder': '+Ve Mark', "class": "form-control"}),
            'minus3': forms.TextInput(attrs={'placeholder': '-Ve Mark', "class": "form-control"}),
            'Type3': forms.CheckboxInput(attrs={'checked': 'checked', 'hidden': ""}),
        }



class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestions
        exclude = ('quiz', 'exam', 'practice',
                   'Type1', 'Questions', 'Option_1',
                   'Option_2', 'Option_3', 'Option_4', 'TrueAns', 'marks1',
                   'minus1',
                   'Type2', 'Question', 'Option1', 'Option2', 'Option3', 'Option4',
                   'Answer1', 'Answer2', 'Answer3', 'Answer4', 'marks2', 'minus2',
                   'Type3', 'Que', 'Answer31', 'Answer32', 'marks3', 'minus3'
                   )

        widgets = {
            'Ques_tion': RichTextUploadingFormField(),
            'TrueAns1': forms.Select(attrs={'class': 'form-control show-tick', "required": ''
                                           }),
            'marks4': forms.TextInput(attrs={'placeholder': '+Ve Mark', "class": "form-control"}),
            'minus4': forms.TextInput(attrs={'placeholder': '-Ve Mark', "class": "form-control"}),
            'Type4': forms.CheckboxInput(attrs={'checked': 'checked', 'hidden': ""}),

        }




class QuestionsForm(ModelForm):
    class Meta:
        model = MultipleChoiceQuestions
        fields = ['Question', 'TrueAns']

