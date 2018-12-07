from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "LibraryPanel"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Library_Add_Category,name = 'Library_add_cat'),
    url(r'^Book_List/$', Library_Book_List,name = 'Library_book_List'),
    url(r'^Add_Book_Sub_Category/$', Library_add_sub_category,name = 'Library_add_sub_cat'),
    url(r'^Library_add_books/(?P<cat>[\w-]+)/$', Library_Add_Books,name = 'Library_add_books'),
    url(r'^Library_books_Details/(?P<bid>[0-9]+)/$', Library_book_details,name = 'Library_book_details'),
    url(r'^Library_books_Edit_Details/(?P<bid>[0-9]+)/$', Library_Book_Edit_Details,name = 'Library_book_edit'),
    url(r'^Library_online_books/$', Library_Online_Book, name = 'Library_online_book'),
    url(r'^Library_add_e_books/(?P<cat>[\w-]+)/$', Library_E_Add_Books, name='Library_add_e_books'),
    url(r'^Library_delete_e_book/(?P<bid>[0-9]+)/$', Library_Online_Delete_Book, name='Library_delete_book'),

    url(r'^Library_issue_books/(?P<bid>[0-9]+)/(?P<cour>[\w-]+)/(?P<bch>[\w-]+)/(?P<stu>[\w-]+)/$', Library_Book_Issue, name = 'Library_issue_book'),
url(r'^Library_issued_books/$', Library_Issued_Books, name = 'Library_issued_book'),
url(r'^Library_Return_Book/(?P<bid>[0-9]+)/$', Library_Return_Book,name = 'Library_Return_Book'),

]