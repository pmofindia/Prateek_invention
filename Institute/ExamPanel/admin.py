from django.contrib import admin

from .models import *

admin.site.register(ExamPackage)
admin.site.register(MainExam)
admin.site.register(MultipleChoiceQuestions)
admin.site.register(SubPackage_MainExam)