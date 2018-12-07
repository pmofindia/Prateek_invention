from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "StudentPanel"
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', Dashboard, name = 'home'),
url(r'^test_list/$', AllTests, name = 'tests'),
url(r'^test_instruction/$', TestInstruction, name = 'instruction'),
url(r'^test_live/$', LiveTest, name = 'live'),
url(r'^analysis/$', TestAnalysis, name = 'analysis'),

url(r'^practice/$', Practice, name = 'practice'),
url(r'^practice_questions/$', PracticeQuestion, name = 'practice_questions'),
url(r'^single_question/$', StartPractice, name = 'single_question'),

url(r'^quiz/$', Quiz, name = 'quiz'),
url(r'^start_quiz/$', StartQuiz, name = 'start_quiz'),
url(r'^quiz_summery/$', QuizSummery, name = 'quiz_summery'),



url(r'^study_material/$', StudyMaterial, name = 'study_material'),
url(r'^courses/$', Courses, name = 'courses'),
url(r'^fee/$', FeeDetails, name = 'FeeDetails'),
url(r'^invoice/$', Invoice, name = 'invoice'),
]