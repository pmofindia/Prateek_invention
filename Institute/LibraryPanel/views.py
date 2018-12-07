from django.shortcuts import render, redirect
from Institute.models import *
from datetime import date,datetime


def Library_Add_Category(request):
    all_cat = Master_catbook_data.objects.all()
    if request.method == "POST":
        cat_book = request.POST['cat_book']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_catbook_data.objects.create(name=cat_book, created_date=format_date)
        return redirect("LibraryPanel:Library_add_cat")
    return render(request,'Library/master_cat_book.html',{"all_cat":all_cat})


def Library_add_sub_category(request):
    all_cat = Master_catbook_data.objects.all()
    if request.method == "POST":
        cat_book = request.POST['cat_book']
        cat = Master_catbook_data.objects.filter(id = cat_book).first()
        subcat_book = request.POST['subcat_book']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        Master_subcatbook_data.objects.create(category=cat, name=subcat_book, created_date=format_date)
        return redirect('LibraryPanel:Library_add_sub_cat')
    return render(request,'Library/master_sub_book.html',{"all_cat":all_cat})

def Library_Book_List(request):
    all_book =  Master_book_data.objects.all()
    return render(request,'Library/master_book.html',{"all_book":all_book})


def Library_Add_Books(request, cat):
    sub_category = []
    if cat == "ALL":
        all_category = Master_catbook_data.objects.all()
    else:
        all_category = Master_catbook_data.objects.filter(id=cat)
        category = Master_catbook_data.objects.filter(id = cat).first()
        sub_category = Master_subcatbook_data.objects.filter(category = category)
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
        sub_cat = Master_subcatbook_data.objects.filter(id=subcategory).first()
        cat = Master_catbook_data.objects.filter(id = cat).first()

        Master_book_data.objects.create(category=cat, subcategory=sub_cat, book_title=title
                                        , subbook_title=subtitle, ISBN=ISBN, author=author, publisher=publisher
                                        , created_date=format_date, editor=editor, series=series,
                                        publication_year=publisher_year, edition=edition, type=type
                                        , pages=total_page, copies=copies)

        return redirect('LibraryPanel:Library_book_List')
    return render(request, 'Library/master_add_book.html', {"all_category": all_category, 'cat':sub_category, 'cat_n':cat})

def Library_book_details(request, bid):
    book =  Master_book_data.objects.filter(id=bid).first()
    return render(request,'Library/master_book_detail.html',{"book":book})


def Library_Book_Edit_Details(request, bid):
    book = Master_book_data.objects.filter(id=bid).first()
    if request.method == "POST":
        d = request.POST
        book.book_title = d['title']
        book.subbook_title = d['subtitle']
        book.ISBN = d['isbn']
        book.author = d['author']
        book.publisher = d['publisher']
        book.editor = d['editor']
        book.series = d['series']
        book.publication_year = d['publisher_year']
        book.edition = d['edition']
        book.pages = d['total_page']
        book.copies = d['copies']
        book.save()
        return redirect("LibraryPanel:Library_book_details", bid)
    return render(request, "Library/master_edit_book_details.html", {'book':book})

def Library_Online_Book(request):
    all_book = Master_E_Book.objects.all()
    return render(request, 'Library/master_e_book.html',{"all_book":all_book} )

def Library_E_Add_Books(request, cat):
    sub_category = []
    if cat == "ALL":
        all_category = Master_catbook_data.objects.all()
    else:
        all_category = Master_catbook_data.objects.filter(id=cat)
        category = Master_catbook_data.objects.filter(id = cat).first()
        sub_category = Master_subcatbook_data.objects.filter(category = category)
    if request.method == "POST":
        title = request.POST['title']
        subcategory = request.POST['subcategory']
        author = request.POST['author']
        publisher = request.POST['publisher']
        book = request.FILES['file']
        today = date.today()
        format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
        sub_cat = Master_subcatbook_data.objects.filter(id=subcategory).first()
        cat = Master_catbook_data.objects.filter(id = cat).first()

        Master_E_Book.objects.create(category=cat, subcategory=sub_cat, book_title=title
                                        ,author=author, publisher=publisher, book = book
                                        ,created_date=format_date)

        return redirect('LibraryPanel:Library_online_book')
    return render(request, 'Library/master_add_e_book.html', {"all_category": all_category, 'cat':sub_category, 'cat_n':cat})


def Library_Online_Delete_Book(request, bid):
    all_book = Master_E_Book.objects.filter(id = bid).first()
    all_book.delete()
    return redirect("LibraryPanel:Library_online_book")



def Library_Book_Issue(request, bid, cour, bch, stu):
    book = Master_book_data.objects.filter(id=bid).first()
    batch= []
    students = []
    if cour == "ALL":
        course = Master_course_data.objects.all()
    else:
        course = Master_course_data.objects.filter(id = cour)
        if bch == "ALL":
            batch = Master_batch_data.objects.filter(course = course.first())
        else:
            batch = Master_batch_data.objects.filter(id = bch)
            if stu == "ALL":
                students = Register_Student.objects.filter(course = course, batch = batch)
            else:
                students = Register_Student.objects.filter(id = stu)
    if request.method == "POST":
        d = request.POST
        iss = d['issue']
        du = d['return']
        Library_Issue_Book.objects.create(book = book, student = students.first(),
                                          issue = iss, Due = du, status = "Issued")

        return redirect('LibraryPanel:Library_book_List')
    return render(request, 'Library/master_issue_book.html', {'book':book, 'courses':course,
                                                              'cour':cour, 'batches':batch,'bch':bch,
                                                                  'students':students, 'stu':stu})


def Library_Issued_Books(request):
    books = Library_Issue_Book.objects.filter(status = "Issued")
    return render(request, "Library/create_exam_package.html", {'books':books})



def Library_Return_Book(request, bid):
    book = Library_Issue_Book.objects.filter(id = bid).first()
    today = date.today()
    format_date = datetime.strptime(str(today), "%Y-%m-%d").strftime('%d/%m/%Y')
    dt1 = book.Due.split('-')
    dt1 = ''.join(dt1)
    dt2 = format_date.split('/')
    dt2.reverse()
    dat = dt2
    dt2 = ''.join(dt2)
    dif = int(dt1)-int(dt2)
    data = LateFine.objects.filter().first()
    fine = 0
    if dif < 0:
        days = abs(dif)
        fine = days * int(data.libraryfine)
        book.status = "Fine"
    else:
        book.status = "Returned"
        book.Return = '-'.join(dat)
    book.late_fee = fine
    book.save()
    return redirect('LibraryPanel:Library_issued_book')