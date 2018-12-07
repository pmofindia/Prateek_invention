from django.conf.urls import url,include
from django.contrib import admin
from Frontdesk.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Frontdesk"
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name = 'home'),
    url(r'^add-StudentHome/$', Front_add_student,name = 'front_add_student'),
    url(r'^enquiry_list$', Front_enquiry, name='front_enquiry'),
    url(r'^details_enquiry/(?P<eid>[0-9]+)/$', Front_view_enquiry, name='front_view_enquiry'),
               ]