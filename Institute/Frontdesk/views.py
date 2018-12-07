from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
def home(request):
    return render(request,'front/top.html')


def Front_add_student(request,num):
    form = Student_form()
    batch = False
    if num != 'Add':
       cor =  Master_course_data.objects.filter(id = num).first()
       batch = cor.master_batch_data_set.all()
    if request.method == "POST":
        form = Student_form(request.POST)
        if form.is_valid():
            d = form.cleaned_data



    return render(request,'front/front_add_student.html',{"form":form,"batch":batch})

def Front_enquiry(request):
    form = Enquiry_form()
    all_enquiry = Front_enquiry_data.objects.all()
    if request.method == "POST":
        form = Enquiry_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    return render(request,'front/front_enquiry.html',{"form":form,"all_enquiry":all_enquiry})


def Front_view_enquiry(request,eid):
    data = Front_enquiry_data.objects.get(id = eid)
    return render(request,'front/front_view_enquiry.html',{"data":data})