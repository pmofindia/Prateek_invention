from django.shortcuts import render

def Dashboard(request):
    return render(request, "StudentHome/dashboard.html")

def AllTests(request):
    return render(request, "StudentHome/all_test.html")

def TestInstruction(request):
    return render(request, "StudentHome/instruction.html")

def LiveTest(request):
    return render(request, "StudentHome/live_test.html")

def TestAnalysis(request):
    return render(request, "StudentHome/test_analysis.html")

def Practice(request):
    return render(request, "StudentHome/practice.html")

def PracticeQuestion(request):
    return render(request, "StudentHome/practice_questions.html")

def StartPractice(request):
    return render(request, "StudentHome/single_question.html")

def Quiz(request):
    return render(request, "StudentHome/quiz.html")

def StartQuiz(request):
    return render(request, "StudentHome/start_quiz.html")

def QuizSummery(request):
    return render(request, "StudentHome/quiz_summery.html")

def StudyMaterial(request):
    return render(request, "StudentHome/studyMaterial.html")

def Courses(request):
    return render(request, "StudentHome/Courses.html")

def FeeDetails(request):
    return render(request, "StudentHome/fee.html")

def Invoice(request):
    return render(request, "StudentHome/invoice.html")
