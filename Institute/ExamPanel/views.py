from django.shortcuts import render, redirect
from .forms import *
import itertools
from django.http import HttpResponse


def Home(request):
    return render(request, "exam/create_exam_package.html")


def CreateExamPackage(request):
    data = ExamPackage.objects.all().order_by('-id')
    form = CreateExamPackageForm()
    if request.method == "POST":
        form = CreateExamPackageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("ExamPanel:create_exam_package")
    return render(request, "exam/create_exam_package.html", {"form":form, 'packages':data})


def EditExamPackage(request, eid):
    data = ExamPackage.objects.filter(id = eid).first()
    form = CreateExamPackageForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:create_exam_package")

    return render(request, "exam/edit_exam_package.html", {"form":form})



def AddExamSubPackage(request, eid):
    pack = ExamPackage.objects.filter(id = eid).first()
    sub = Package_Subpackage.objects.filter(package = pack)
    courses = Master_course_data.objects.all()
    if request.method == "POST":
        d = request.POST.getlist('checks')
        for i in d:
            n = 0
            for j in sub:
                if i == str(j.sub.id):
                    n = n+1
            if n == 0:
                s = ExamSubPackage.objects.filter(id = i).first()
                Package_Subpackage.objects.create(package=pack, sub = s)
        return redirect("ExamPanel:add_packages", eid)

    context = {
        'subpackages':sub,
        'courses':courses
    }
    return render(request, "exam/sub_packages_list.html", context)



def RemoveSubPackage(request, eid):
    d = Package_Subpackage.objects.filter(id = eid).first()
    d.delete()
    return redirect(request.META.get('HTTP_REFERER'))



def GetValue(request):
    if request.method == "POST":
        d = request.POST.getlist('checks')
        if d:
            print(d)
            return HttpResponse(d)
    return render(request, "exam/checkValue.html")



def DeleteExamPackage(request, eid):
    data = ExamPackage.objects.filter(id = eid).first()
    data.delete()
    return redirect("ExamPanel:create_exam_package")



def CreateExamSubPackage(request, cour, pack):
    data = ExamSubPackage.objects.all().order_by('-id')
    form = CreateExamSubPackageForm()
    course = Master_course_data.objects.all()
    pck = []
    form = CreateMainExamForm()
    cou = 0
    if cour != "0":
        cou = Master_course_data.objects.filter(id=cour).first()
        pck = ExamPackage.objects.filter(course=cou)
    if request.method == "POST":
        if pack == '0':
            return redirect("ExamPanel:create_exam_subpackage", cour, '0')
        form = CreateExamSubPackageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            data.course = cou
            data.save()
            pac = ExamPackage.objects.filter(id = pack).first()
            Package_Subpackage.objects.create(package = pac, sub = data)
            return redirect("ExamPanel:create_exam_subpackage", '0', '0')
    context = {
        'course': course, "icour": int(cour), "cour": cour,
        'package': pck, 'ipack': int(pack), 'pack': pack,
        'exams': data, 'form': form, 'subpackages':data
        }
    return render(request, "exam/create_exam_subpackage.html", context)


def ExamSubPackageDetails(request, eid, cour, pack):
    sub = ExamSubPackage.objects.filter(id = eid).first()
    data = Package_Subpackage.objects.filter(sub = sub)
    course = Master_course_data.objects.all()
    pck = []
    Packs = []
    if cour != "0":
        cou = Master_course_data.objects.filter(id=cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        for i in pck:
            n = 0
            for j in data:
                if i == j.package:
                    n += 1
            if n == 0:
                Packs.append(i)
    if request.method == "POST":
        if cour == "0" or pack == "0":
            return redirect("ExamPanel:subpackage_details", 'eid', cour, pack)
        package = ExamPackage.objects.filter(id = pack).first()
        Package_Subpackage.objects.create(package = package, sub = sub)
        return redirect("ExamPanel:subpackage_details", eid, '0', '0')

    context = {
        'course': course, "icour": int(cour), "cour": cour,
        'package': Packs, 'ipack': int(pack), 'pack': pack,
        'exams': data, 'packages': data, 'eid':eid
                }
    return render(request, "exam/exam_subpackage_details.html", context)



def EditExamSubPackage(request, eid):
    data = ExamSubPackage.objects.filter(id = eid).first()
    form = CreateExamSubPackageForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:create_exam_subpackage", '0', '0')

    return render(request, "exam/edit_exam_subpackage.html", {"form":form})


def DeleteExamSubPackage(request, eid):
    data = ExamSubPackage.objects.filter(id = eid).first()
    data.delete()
    return redirect("ExamPanel:create_exam_subpackage", '0', '0')



def CreateMainExam(request, cour, pack, subpack):
    data = MainExam.objects.all().order_by('-id')
    course = Master_course_data.objects.all()
    d = ExamSubPackage.objects.filter(id=subpack).first()
    pck = []
    sub = []
    cou = 0
    form = CreateMainExamForm()
    if cour != "0":
        cou = Master_course_data.objects.filter(id = cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        if pack != '0':
            pc = ExamPackage.objects.filter(id = pack).first()
            sub = Package_Subpackage.objects.filter(package = pc)
    if request.method == "POST":
        form = CreateMainExamForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.course = cou
            data.save()
            s = ExamSubPackage.objects.filter(id = subpack).first()
            SubPackage_MainExam.objects.create(sub = s, main = data)
            return redirect("ExamPanel:create_main_exam", '0', '0', '0')
    context = {
        'course': course, "icour": int(cour), "cour": cour,
        'package': pck, 'ipack': int(pack), 'pack': pack,
        'subpackage': sub, 'isubpack': int(subpack), 'subpack': subpack,
        'exams': data, 'form':form
    }
    return render(request, "exam/create_main_exam.html", context)



def MainExamDetails(request, eid, cour, pack, subpack):
    sub = MainExam.objects.filter(id = eid).first()
    data = SubPackage_MainExam.objects.filter(main = sub)
    course = Master_course_data.objects.all()
    pck = []
    Packs = []
    if cour != "0":
        cou = Master_course_data.objects.filter(id=cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        if pack != "0":
            pkg = ExamPackage.objects.filter(id = pack).first()
            subpackage = Package_Subpackage.objects.filter(package = pkg)
            for i in subpackage:
                n = 0
                for j in data:
                    if i.sub == j.sub:
                        n += 1
                if n == 0:
                    Packs.append(i)
    if request.method == "POST":
        if cour == "0" or pack == "0" or subpack == "0":
            return redirect("ExamPanel:main_exam_details", 'eid', cour, pack, subpack)
        subpackage = ExamSubPackage.objects.filter(id = subpack).first()
        SubPackage_MainExam.objects.create(sub = subpackage, main = sub)
        return redirect("ExamPanel:main_exam_details", eid, '0', '0', '0')

    context = {
        'course': course, "icour": int(cour), "cour": cour,
        'package': pck, 'ipack': int(pack), 'pack': pack,
        'subpackage':Packs, 'isubpack':int(subpack), 'subpack':subpack,
        'exams': data, 'packages': data, 'eid':eid
                }
    return render(request, "exam/main_exam_details.html", context)


def RemoveMainExam(request, eid):
    d = SubPackage_MainExam.objects.filter(id = eid).first()
    d.delete()
    return redirect(request.META.get('HTTP_REFERER'))




def EditMainExam(request, eid):
    data = MainExam.objects.filter(id = eid).first()
    form = CreateMainExamForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:create_main_exam", '0', '0', '0')
    return render(request, "exam/edit_main_exam.html", {"form":form})



def ExamInstructionView(request, eid):
    data = MainExam.objects.filter(id=eid).first()
    return render(request, "exam/exam_instruction.html", {"data":data})


def AllQuestions(request, cour, pack, subpack, exam):
    print(type(cour))
    course = Master_course_data.objects.all()
    pck = []
    sub = []
    exams = []
    if cour != "0":
        cou = Master_course_data.objects.filter(id = cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        if pack != '0':
            pc = ExamPackage.objects.filter(id = pack).first()
            sub = ExamSubPackage.objects.filter(package = pc)
            if subpack != '0':
                sb = ExamSubPackage.objects.filter(id = subpack).first()
                exams = MainExam.objects.filter(Sub_package = sb)

    context = {
        'course':course, "icour":int(cour), "cour":cour,
        'package':pck, 'ipack':int(pack), 'pack':pack,
        'subpackage':sub, 'isubpack':int(subpack), 'subpack':subpack,
        'exams':exams, 'iexam':int(exam), 'exam':exam
    }
    return render(request, "exam/all_questions.html", context)


def AddImportQuestions(request, cour, pack, subpack, exam):
    print(type(cour))
    course = Master_course_data.objects.all()
    pck = []
    sub = []
    exams = []
    if cour != "0":
        cou = Master_course_data.objects.filter(id = cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        if pack != '0':
            pc = ExamPackage.objects.filter(id = pack).first()
            sub = ExamSubPackage.objects.filter(package = pc)
            if subpack != '0':
                sb = ExamSubPackage.objects.filter(id = subpack).first()
                exams = MainExam.objects.filter(Sub_package = sb)

    context = {
        'course':course, "icour":int(cour), "cour":cour,
        'package':pck, 'ipack':int(pack), 'pack':pack,
        'subpackage':sub, 'isubpack':int(subpack), 'subpack':subpack,
        'exams':exams, 'iexam':int(exam), 'exam':exam
    }
    return render(request, "exam/add_import_questions.html", context)


def AddMainExamSection(request, cour, pack, subpack, exam):
    course = Master_course_data.objects.all()
    pck = []
    sub = []
    exams = []
    if cour != "0":
        cou = Master_course_data.objects.filter(id = cour).first()
        pck = ExamPackage.objects.filter(course=cou)
        if pack != '0':
            pc = ExamPackage.objects.filter(id = pack).first()
            sub = Package_Subpackage.objects.filter (package = pc)
            if subpack != '0':
                sb = ExamSubPackage.objects.filter(id = subpack).first()
                exams = SubPackage_MainExam.objects.filter(sub = sb)
                if exam != '0':
                    return redirect('ExamPanel:exam_section', cour, pack, subpack, exam)

    context = {
        'course':course, "icour":int(cour), "cour":cour,
        'package':pck, 'ipack':int(pack), 'pack':pack,
        'subpackage':sub, 'isubpack':int(subpack), 'subpack':subpack,
        'exams':exams, 'iexam':int(exam), 'exam':exam
    }
    return render(request, "exam/add_main_exam_section.html", context)


def ExamSectionCreation(request, cour, pack, subpack, eid):
    if eid == '0':
        return redirect("ExamPanel:add_main_exam_section", cour, pack, subpack, eid)
    exam = MainExam.objects.filter(id = eid).first()
    sections = MainExamSection.objects.filter(exam = exam)
    if request.method == "POST":
        d = request.POST
        s = []
        for i in range(1, 6):
            if d['s'+ str(i)]:
                s.append(d['s'+str(i)])
        exam = MainExam.objects.filter(id = eid).first()
        for i in s:
            MainExamSection.objects.create(exam = exam, name = i)
    context = {
        "cour": cour, 'sections':sections,
        'pack': pack,
        'subpack': subpack,
        'exam': eid
        }
    return render(request, "exam/exam_sections.html", context)


def ExamSectionDelete(request, sid, cour, pack, subpack, eid ):
    data = MainExamSection.objects.filter(id = sid).first()
    data.delete()
    return redirect("ExamPanel:exam_section", cour, pack, subpack, eid )


def FilteredQuestions(request, cid, pid, spid, eid):
    iterator = itertools.count()
    if cid == '0':
        return redirect("ExamPanel:all_questions", '0', '0', '0', '0')
    elif pid == '0':
        ques_tion = []
        d = Master_course_data.objects.filter(id = cid).first()
        que = ExamPackage.objects.filter(course = d)
        for pack in que:
            for sub in pack.examsubpackage_set.all():
                for exam in sub.mainexam_set.all():
                    for ques in exam.multiplechoicequestions_set.all():
                        ques_tion.append(ques)

        return render(request, "exam/exam_questions.html", {'questions': ques_tion, 'iterator':iterator})

    elif spid == '0':
        ques_tion = []
        d = ExamPackage.objects.filter(id = pid).first()
        subpack = ExamSubPackage.objects.filter(package = d)
        for sub in subpack:
            for exam in sub.mainexam_set.all():
                for ques in exam.multiplechoicequestions_set.all():
                    ques_tion.append(ques)
        return render(request, "exam/exam_questions.html", {'questions': ques_tion, 'iterator':iterator})

    elif eid == '0':
        ques_tion = []
        d = ExamSubPackage.objects.filter(id = spid).first()
        que = MainExam.objects.filter(Sub_package = d)
        for exam in que:
            for ques in exam.multiplechoicequestions_set.all():
                ques_tion.append(ques)
        return render(request, "exam/exam_questions.html", {'questions': ques_tion, 'iterator':iterator})

    else:
        ques_tion = []
        d = MainExam.objects.filter(id = eid).first()
        que = MultipleChoiceQuestions.objects.filter(exam = d)
        for ques in que:
            ques_tion.append(ques)
        return render(request, "exam/exam_questions.html", {'questions': ques_tion, 'iterator':iterator})



def TypeofQuestion(request, eid, type):
    if request.method == "POST":
        Type = request.POST['questionType']
        if Type == "0":
            return redirect('ExamPanel:select_question_type', eid, type)
        if Type == "multi":
            return redirect("ExamPanel:add_multi_questions", eid)
        if Type == "response":
            return redirect("ExamPanel:add_multi_response_questions", eid)
        if Type == "blank":
            return redirect("ExamPanel:add_fill_questions", eid)
        if Type == "truefalse":
            return redirect("ExamPanel:add_true_false_questions", eid)
    return render(request, "exam/questionType.html")



def AddMultiQuestions(request, eid):
    d = MainExam.objects.filter(id=eid).first()
    form = MultiChoiseQuestionForm()
    if request.method == "POST":
        form = MultiChoiseQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            print(data.Questions, data.TrueAns)
            data.exam = d
            data.save()

            return redirect("ExamPanel:add_multi_questions", eid)
    return render(request, "exam/multiquestion.html", {"form":form})



def EditMultiQuestions(request, eid):
    data = MultipleChoiceQuestions.objects.filter(id = eid).first()
    form = MultiChoiseQuestionForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:filter_questions", '0')
    return render(request, "exam/edit_multiquestion.html", {"form":form})


def AddMultiResponseQuestions(request, eid):
    d = MainExam.objects.filter(id=eid).first()
    form = MultiResponseQuestionForm()
    if request.method == "POST":
        form = MultiResponseQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.exam = d
            data.save()
            return redirect("ExamPanel:add_multi_response_questions", eid)
    return render(request, "exam/multiresponsequestion.html", {"form":form})


def EditMultiResponseQuestions(request, eid):
    data = MultipleChoiceQuestions.objects.filter(id = eid).first()
    form = MultiResponseQuestionForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:filter_questions", '0')
    return render(request, "exam/edit_multiresponsequestion.html", {"form":form})




def AddFillInTheBlanksQuestions(request, eid):
    d = MainExam.objects.filter(id=eid).first()
    form = FillInTheBlankQuestionForm()
    if request.method == "POST":
        form = FillInTheBlankQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.exam = d
            data.save()
            return redirect("ExamPanel:add_fill_questions", eid)
    return render(request, "exam/Fillquestion.html", {"form":form})


def EditFillInTheBlanksQuestions(request, eid):
    data = MultipleChoiceQuestions.objects.filter(id = eid).first()
    form = FillInTheBlankQuestionForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:filter_questions", '0')
    return render(request, "exam/edit_Fillquestion.html", {"form":form})



def AddTrueFalseQuestions(request, eid):
    d = MainExam.objects.filter(id=eid).first()
    form = TrueFalseQuestionForm()
    if request.method == "POST":
        form = TrueFalseQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.exam = d
            data.save()
            return redirect("ExamPanel:add_fill_questions", eid)
    return render(request, "exam/truefalse.html", {"form":form})



def EditTrueFalseQuestions(request, eid):
    data = MultipleChoiceQuestions.objects.filter(id = eid).first()
    form = TrueFalseQuestionForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        data = form.save(commit=False)
        data.save()
        return redirect("ExamPanel:filter_questions", '0')
    return render(request, "exam/edit_truefalse.html", {"form":form})




