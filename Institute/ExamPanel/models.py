from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from Institute.models import *


class ExamPackage(models.Model):
    course = models.ForeignKey(Master_course_data, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)
    syllabus = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name + "------" + self.course.name



class ExamSubPackage(models.Model):
    course = models.ForeignKey(Master_course_data, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    syllabus = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class Package_Subpackage(models.Model):
    package = models.ForeignKey(ExamPackage, on_delete=models.SET_NULL, null=True)
    sub = models.ForeignKey(ExamSubPackage, on_delete=models.SET_NULL, null=True)



class MainExam(models.Model):
    course = models.ForeignKey(Master_course_data, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)
    instruction = RichTextUploadingField(blank=True, null=True)
    syllabus = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class SubPackage_MainExam(models.Model):
    sub = models.ForeignKey(ExamSubPackage, on_delete=models.SET_NULL, null=True)
    main = models.ForeignKey(MainExam, on_delete=models.SET_NULL, null=True)



class MainExamSection(models.Model):
    exam = models.ForeignKey(MainExam, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name



class QuizPackage(models.Model):
    course = models.ForeignKey(Master_course_data, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True, default=0)
    syllabus = models.FileField(null=True, blank=True)


class Quiz(models.Model):
    package = models.ForeignKey(QuizPackage, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    syllabus = models.FileField(null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)



class DealyPractice(models.Model):
    course = models.ForeignKey(Master_course_data, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True, default=0)
    syllabus = models.FileField(null=True, blank=True)


class Topic(models.Model):
    package = models.ForeignKey(QuizPackage, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    syllabus = models.FileField(null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)


Ans = [
    ['1', '1'],
    ['2', '2'],
    ['3', '3'],
    ['4', '4'],
]


Ans1 = [
    ['1', 'True'],
    ['2', 'False']
]



class MultipleChoiceQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, blank=True)
    exam = models.ForeignKey(MainExam, on_delete=models.SET_NULL, null=True, blank=True)

    section = models.ForeignKey(MainExamSection, on_delete=models.SET_NULL, null=True, blank=True )

    practice = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)

    Type1 = models.BooleanField(default=False)
    Questions = RichTextUploadingField(blank=True, null=True)
    Option_1 = RichTextUploadingField(blank=True, null=True)
    Option_2 = RichTextUploadingField(blank=True, null=True)
    Option_3 = RichTextUploadingField(blank=True, null=True)
    Option_4 = RichTextUploadingField(blank=True, null=True)
    TrueAns = models.CharField(max_length=5, choices=Ans, default='1')
    marks1 = models.CharField(max_length=5, null=True, blank=True)
    minus1 = models.CharField(max_length=20, default=0)

    Type2 = models.BooleanField(default=False)
    Question = RichTextUploadingField(blank=True, null=True)
    Option1 = RichTextUploadingField(blank=True, null=True)
    Option2 = RichTextUploadingField(blank=True, null=True)
    Option3 = RichTextUploadingField(blank=True, null=True)
    Option4 = RichTextUploadingField(blank=True, null=True)
    Answer1 = models.BooleanField(default=False)
    Answer2 = models.BooleanField(default=False)
    Answer3 = models.BooleanField(default=False)
    Answer4 = models.BooleanField(default=False)
    marks2 = models.CharField(max_length=5, null=True, blank=True)
    minus2 = models.CharField(max_length=20, default=0)

    Type3 = models.BooleanField(default=False)
    Que = RichTextUploadingField(blank=True, null=True)
    Answer31 = models.CharField(max_length=250, null=True, blank=True)
    Answer32 = models.CharField(max_length=250, null=True, blank=True)
    marks3 = models.CharField(max_length=5, null=True, blank=True)
    minus3 = models.CharField(max_length=20, default=0)

    Type4 = models.BooleanField(default=False)
    Ques_tion = RichTextUploadingField(blank=True, null=True)
    TrueAns1 = models.CharField(max_length=5, choices=Ans1, default='1')
    marks4 = models.CharField(max_length=5, null=True, blank=True)
    minus4 = models.CharField(max_length=20, default=0)




class StudyMaterial(models.Model):
    topic = models.CharField(max_length=250, null=True, blank=True)

class CurrentAffairs(models.Model):
    material = models.ForeignKey(StudyMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    files = models.FileField()

class Bloging(models.Model):
    material = models.ForeignKey(StudyMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)

class Blog(models.Model):
    blog = models.ForeignKey(Bloging, on_delete=models.SET_NULL, null=True, blank=True)
    description = RichTextUploadingField(blank=True, null=True)


