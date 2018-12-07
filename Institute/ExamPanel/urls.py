from django.conf.urls import url,include
from django.contrib import admin
from Institute.views import *
from django.conf import settings
from django.conf.urls.static import static
from ExamPanel.views import *

app_name = "ExamPanel"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/$', Home, name='exam_home'),
    url(r'^values/$', GetValue, name='value'),
    url(r'^create_exam_package/$', CreateExamPackage, name='create_exam_package'),
url(r'^delete_exam_package/(?P<eid>[0-9]+)/$', DeleteExamPackage, name='delete_package'),
url(r'^edit_exam_package/(?P<eid>[0-9]+)/$', EditExamPackage, name='edit_package'),
url(r'^add_exam_sub_packages/(?P<eid>[0-9]+)/$', AddExamSubPackage, name='add_packages'),
url(r'^remove_sub_packages/(?P<eid>[0-9]+)/$', RemoveSubPackage, name='remove_sub_packages'),

    url(r'^create_exam_subpackage/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/$', CreateExamSubPackage, name='create_exam_subpackage'),
    url(r'^details_exam_subpackage/(?P<eid>[\w-]+)/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/$', ExamSubPackageDetails, name='subpackage_details'),
    url(r'^edit_subpackage/(?P<eid>[0-9]+)/$', EditExamSubPackage, name='edit_subpackage'),
    url(r'^delete_exam_subpackage/(?P<eid>[0-9]+)/$', DeleteExamSubPackage, name='delete_subpackage'),



url(r'^create_main_exam/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/$', CreateMainExam, name='create_main_exam'),
    url(r'^edit_main_exam/(?P<eid>[0-9]+)/$', EditMainExam, name='edit_main'),
url(r'^exam_instruction/(?P<eid>[0-9]+)/$', ExamInstructionView, name='exam_instruction'),
url(r'^main_exam_details/(?P<eid>[0-9]+)/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/$', MainExamDetails, name='main_exam_details'),
url(r'^remove_main_exams/(?P<eid>[0-9]+)/$', RemoveMainExam, name='remove_main_exam'),

    url(r'^all_questions/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/(?P<exam>[\w-]+)/$', AllQuestions, name='all_questions'),
url(r'^add_import_questions/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/(?P<exam>[\w-]+)/$', AddImportQuestions, name='add_import_questions'),
url(r'^add_main_exam_section/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/(?P<exam>[\w-]+)/$', AddMainExamSection, name='add_main_exam_section'),
url(r'^exam_section/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/(?P<eid>[0-9]+)/$', ExamSectionCreation, name='exam_section'),

url(r'^delete_exam_section/(?P<sid>[\w-]+)/(?P<cour>[\w-]+)/(?P<pack>[\w-]+)/(?P<subpack>[\w-]+)/(?P<eid>[0-9]+)/$', ExamSectionDelete, name='delete_exam_section'),


url(r'^filter_questions/(?P<cid>[0-9]+)/(?P<pid>[0-9]+)/(?P<spid>[0-9]+)/(?P<eid>[0-9]+)/$', FilteredQuestions, name='filter_questions'),


url(r'^select_question_type/(?P<eid>[\w-]+)/(?P<type>[\w-]+)/$', TypeofQuestion, name='select_question_type'),


url(r'^add_multi_questions/(?P<eid>[0-9]+)/$', AddMultiQuestions, name='add_multi_questions'),
url(r'^add_multi_response_questions/(?P<eid>[0-9]+)/$', AddMultiResponseQuestions, name='add_multi_response_questions'),
url(r'^add_fill_questions/(?P<eid>[0-9]+)/$', AddFillInTheBlanksQuestions, name='add_fill_questions'),
url(r'^add_true_false_questions/(?P<eid>[0-9]+)/$', AddTrueFalseQuestions, name='add_true_false_questions'),


url(r'^edit_multi_questions/(?P<eid>[0-9]+)/$', EditMultiQuestions, name='edit_multi_questions'),
url(r'^edit_multi_response_questions/(?P<eid>[0-9]+)/$', EditMultiResponseQuestions, name='edit_multi_response_questions'),
url(r'^edit_fill_questions/(?P<eid>[0-9]+)/$', EditFillInTheBlanksQuestions, name='edit_fill_questions'),
url(r'^edit_true_false_questions/(?P<eid>[0-9]+)/$', EditTrueFalseQuestions, name='edit_true_false_questions'),


    ]




