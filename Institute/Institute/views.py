from django.shortcuts import render,redirect
from .models import *
from datetime import date,datetime

def Delete_All(request, num, type):
    if type == "Fee_Type":
        data = Master_fee_type_data.objects.get(id = num)
        data.delete()

    if type == "Course":
        data = Master_course_data.objects.get(id=num)
        data.delete()

    if type == "Subject":
        data = Master_subject_data.objects.get(id=num)
        data.delete()

    if type == "Category":
        data = Master_catbook_data.objects.get(id=num)
        data.delete()

    if type == "Subcategory":
        data = Master_subcatbook_data.objects.get(id=num)
        data.delete()

    if type == "Book":
        data = Master_book_data.objects.get(id=num)
        data.delete()

    if type == "Medium":
        data = Master_medium_data.objects.get(id=num)
        data.delete()

    if type == "Holiday":
        data = Master_holiday_data.objects.get(id=num)
        data.delete()

    if type == "Designation":
        data = Master_designation_data.objects.get(id=num)
        data.delete()

    if type == "Area":
        data = Master_area_data.objects.get(id=num)
        data.delete()

    if type == "Bus":
        data = Master_bus_data.objects.get(id=num)
        data.delete()

    if type == "Driver":
        data = Master_driver_data.objects.get(id=num)
        data.delete()

    if type == "Batch":
        data = Master_batch_data.objects.get(id=num)
        data.delete()


    return redirect(request.META.get('HTTP_REFERER'))


def Add_to_data(request, type):
    if type == "Fee_Type":
        all_course = Master_course_data.objects.all()
        if request.method == "POST":
            fee_type = request.POST['fee_name']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            Master_fee_type_data.objects.create(name=fee_type,created_date=format_date)
            return redirect('master_fee')

        return render(request, 'exam_add_exam.html',{"all_course":all_course})

    if type == "Course":
        mediums = Master_medium_data.objects.all()
        if request.method == "POST":
            name = request.POST['course']
            med = request.POST['medium']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            Master_course_data.objects.create(name=name, medium = med ,created_date=format_date)
            return redirect('master_course')

        return render(request,'master_add_course.html',{"mediums":mediums})

    if type == "Subject":
        courses = Master_course_data.objects.all()

        if request.method == "POST":
            name = request.POST['subject']
            cor = request.POST['course']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            sub_course = Master_course_data.objects.filter(id = cor).first()
            Master_subject_data.objects.create(course = sub_course,name=name
                                        ,created_date=format_date)
            return redirect('master_subject')

        return render(request,'master_add_subject.html',{"courses":courses})

    if type == "Book":
        all_category = Master_catbook_data.objects.all()
        if request.method == "POST":
            title = request.POST['title']
            subtitle = request.POST['subtitle']
            category = request.POST['category']
            subcategory = request.POST['subcategory']
            ISBN = request.POST['isbn']
            author = request.POST['author']
            publisher = request.POST['publisher']
            editor = request.POST['editor']
            series = request.POST['series']
            publisher_year = request.POST['publisher_year']
            edition = request.POST['edition']
            type = request.POST['type']
            total_page = request.POST['total_page']
            copies = request.POST['copies']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            sub_cat = Master_subcatbook_data.objects.filter(id = subcategory).first()
            cat = Master_catbook_data.objects.filter(id=category).first()

            Master_book_data.objects.create(category = cat,subcategory=sub_cat,book_title= title
                                        ,subbook_title= subtitle,ISBN = ISBN,author = author,publisher = publisher
                                        ,created_date=format_date,editor = editor,series = series,
                                        publication_year = publisher_year,edition = edition,type = type
                                        ,pages = total_page,copies = copies)

            return redirect('master_book')
        return render(request,'master_add_book.html',{"all_category":all_category})

    if type == "Batch":
        courses = Master_course_data.objects.all()

        if request.method == "POST":
            co = request.POST['course']
            name = request.POST['batch']
            start = request.POST['start']
            end = request.POST['end']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            start = start.split(' - ')
            end = end.split(' - ')
            start_date = start[0]
            start_time = start[1]
            end_date = end[0]
            end_time = end[1]
            course = Master_course_data.objects.filter(id = co).first()
            Master_batch_data.objects.create(course = course,name = name,start_date = start_date,
                                             start_time = start_time, end_date = end_date,
                                             end_time = end_time,created_date = format_date)
            return redirect('master_batch')

        return render(request,'master_add_batch.html',{"courses":courses})

    if type == "Holiday":

        if request.method == "POST":
            name = request.POST['holiday']
            dstart = request.POST['start']
            dend = request.POST['end']
            reason = request.POST['reason']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            Master_holiday_data.objects.create(name=name,start_date = dstart,end_date = dend,
                                        reason = reason,created_date=format_date)
            return redirect('master_holiday')

        return render(request,'master_add_holiday.html')


    return redirect(request.META.get('HTTP_REFERER'))

def Master_fee_type(request):

    all_type = Master_fee_type_data.objects.all()
    course = Master_course_data.objects.all()
    return render(request,'exam_exam_list.html',{"all_type":all_type,"course":course})

def Master_course_module(request):

    all_courses = Master_course_data.objects.all()

    return render(request,'master_course_module.html',{"all_courses":all_courses})

def Master_subject(request):

    all_courses = Master_course_data.objects.all()
    return render(request,'master_subject.html',{"all_courses":all_courses})

def Master_fee_packege(request):

    return render(request,'master_fee_packege.html')

def Master_add_fee_packege(request):
    all_course = Master_course_data.objects.all()
    all_feetype = Master_fee_type_data.objects.all()
    fee_id = []
    for i in all_feetype:
        fee_id.append(int(i.id))
    if request.method == "POST":
        c = request.POST['course']
        course = Master_course_data.objects.filter(id=c).first()
        li1 = []
        li = request.POST.getlist('fee')
        for i in li:
            li1.append(request.POST[i])

        return redirect('master_packege')
    return render(request,'master_add_fee_packege.html',{"all_course":all_course,
                                        "all_feetype":all_feetype, 'fee_id':fee_id})

def Master_batch(request):

    all_course = Master_course_data.objects.all()

    return render(request,'master_batch.html',{"all_course":all_course})

def Master_medium(request):
    all_medium = Master_medium_data.objects.all()
    if request.method == "POST":
        medium = request.POST['medium']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_medium_data.objects.create(name=medium, created_date=format_date)

    return render(request, 'master_medium.html', {"all_medium": all_medium})



def Master_employee(request):

    return render(request,'master_employee.html')

def Master_designation(request):
    all_desig = Master_designation_data.objects.all()
    if request.method == "POST":
        desig = request.POST['desig']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_designation_data.objects.create(name=desig, created_date=format_date)

    return render(request, 'master_designation.html', {"all_desig": all_desig})


def Master_inventory(request):

    return render(request,'master_inventory.html')

def Master_vendor(request):

    return render(request,'master_vendor.html')

def Master_terms_con(request):

    return render(request,'master_terms.html')

def Master_area(request):
    all_area = Master_area_data.objects.all()
    if request.method == "POST":
        area = request.POST['area']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_area_data.objects.create(name=area, created_date=format_date)

    return render(request,'master_area.html',{"all_area":all_area})

def Master_event(request):

    return render(request,'master_events.html')

def Master_holiday(request):
    all_holiday = Master_holiday_data.objects.all()
    return render(request,'master_holiday.html',{"all_holiday":all_holiday})

def Master_sms_temp(request):

    return render(request,'master_sms_temp.html')

def Master_sms_id(request):

    return render(request,'master_sms_id.html')

def Master_email_temp(request):

    return render(request,'master_email_temp.html')

def Master_account(request):

    return render(request,'master_account.html')

def Master_tax(request):

    return render(request,'master_tax.html')

def Master_pay_mode(request):

    return render(request,'master_payment_mode.html')

def Master_cat_book(request):
    all_cat = Master_catbook_data.objects.all()
    if request.method == "POST":
        cat_book = request.POST['cat_book']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_catbook_data.objects.create(name=cat_book, created_date=format_date)

    return render(request,'master_cat_book.html',{"all_cat":all_cat})

def Master_sub_book(request):
    all_cat = Master_catbook_data.objects.all()
    if request.method == "POST":
        cat_book = request.POST['cat_book']
        cat = Master_catbook_data.objects.filter(id = cat_book).first()
        subcat_book = request.POST['subcat_book']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_subcatbook_data.objects.create(category=cat, name=subcat_book, created_date=format_date)

    return render(request,'master_sub_book.html',{"all_cat":all_cat})



def Master_book(request):
    all_book =  Master_book_data.objects.all()
    return render(request,'master_book.html',{"all_book":all_book})

def Master_book_details(request,bid):
    book =  Master_book_data.objects.get(id=bid)
    return render(request,'master_book_detail.html',{"book":book})

def Master_route(request):

    return render(request,'master_route.html')

def Master_bus(request):
    all_bus = Master_bus_data.objects.all()
    if request.method == "POST":
        name = request.POST['bus']
        number = request.POST['bus_num']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_bus_data.objects.create(name=name, number = number, created_date=format_date)
    return render(request,'master_bus.html',{"all_bus":all_bus})


def Master_asign_bus(request):

    return render(request,'master_asign_bus.html')

def Master_driver(request):
    all_driver = Master_driver_data.objects.all()
    return render(request,'master_driver.html',{"all_driver":all_driver})

def Master_add_driver(request,opt):
    if opt == 'Add_driver':
        if request.method == "POST":
            name = request.POST['driver']
            image = request.FILES['driver_img']
            number = request.POST['mobile']
            licence = request.POST['licence']
            address = request.POST['address']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            Master_driver_data.objects.create(name=name,image = image, mobile = number,
                                              license_number = licence,address = address,created_date=format_date)
            return redirect('master_driver')
    else:
        data = Master_driver_data.objects.get(id = opt)
        if request.method == "POST":
            name = request.POST['driver']
            image = request.FILES['driver_img']
            number = request.POST['mobile']
            licence = request.POST['licence']
            address = request.POST['address']
            today = date.today()
            format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
            data.image = image
            data.name = name
            data.mobile = number
            data.license_number = licence
            data.address = address
            data.created_date = format_date
            data.save()
            return redirect('master_driver')
        return render(request,'master_add_driver.html',{"data":data})

    return render(request,'master_add_driver.html')


















