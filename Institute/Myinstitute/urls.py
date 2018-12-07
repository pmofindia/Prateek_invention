
from django.conf.urls import url,include
from django.contrib import admin
from Institute.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^frontdesk/', include('Frontdesk.urls', namespace='Frontdesk')),
    url(r'^exam_controller/', include('ExamPanel.urls', namespace='ExamPanel')),
    url(r'^library_panel/', include('LibraryPanel.urls', namespace='LibraryPanel')),
    url(r'^student/', include('Student.urls', namespace='StudentPanel')),
    url(r'^admin/', admin.site.urls),

    url('ckeditor/', include('ckeditor_uploader.urls')),

    #######For Delete and add ##############

    url(r'delete/(?P<num>[0-9]+)/(?P<type>[\w-]+)', Delete_All, name = "delete"),
    url(r'add/(?P<type>[\w-]+)', Add_to_data, name = "add"),


    #### for master fee type ########

    url(r'^master_fee_type/$',Master_fee_type ,name='master_fee' ),


    #### for master course/module ########

    url(r'^master_course/$',Master_course_module ,name='master_course' ),

    #### for master subject########

    url(r'^master_subject/$',Master_subject ,name='master_subject' ),

    #### for master fee packege ########

    url(r'^master_fee_packege/$',Master_fee_packege ,name='master_packege' ),
    url(r'^master_fee_packege/add/$',Master_add_fee_packege ,name='master_add_packege' ),

    #### for master Batch ########

    url(r'^master_batch/$',Master_batch ,name='master_batch' ),

    #### for master medium ########

    url(r'^master_medium/$',Master_medium ,name='master_medium' ),

    #### for master employee ########

    url(r'^master_employee/$',Master_employee ,name='master_employee' ),

    #### for master Designation ########

    url(r'^master_designation/$',Master_designation ,name='master_desig' ),

    #### for master inventory ########

    url(r'^master_inventory/$',Master_inventory ,name='master_inventory' ),

    #### for master vendor ########

    url(r'^master_vendor/$',Master_vendor ,name='master_vendor' ),

    #### for master terms and condition ########

    url(r'^master_terms_condition/$',Master_terms_con ,name='master_terms' ),

    #### for master Area ########

    url(r'^master_area/$',Master_area ,name='master_area' ),


    #### for master Events ########

    url(r'^master_events/$',Master_event ,name='master_event' ),

    #### for master Holiday########

    url(r'^master_holiday/$',Master_holiday ,name='master_holiday' ),

    #### for master SMA Template ########

    url(r'^master_sms_template/$',Master_sms_temp ,name='master_stemp' ),

    #### for master sms sender id ########

    url(r'^master_sender_id/$',Master_sms_id ,name='master_sid' ),

    #### for master email template ########

    url(r'^master_email_template/$',Master_email_temp ,name='master_etemp' ),

    #### for master account ########

    url(r'^master_account/$',Master_account ,name='master_account' ),

    #### for master tax########

    url(r'^master_tax/$',Master_tax ,name='master_tax' ),

    #### for master payment mode ########

    url(r'^master_payment_mode/$',Master_pay_mode ,name='master_paymode' ),

    #### for master category book ########

    url(r'^master_category_book/$',Master_cat_book ,name='master_cat' ),

    #### for master SubCategory book ########

    url(r'^master_sub_book/$',Master_sub_book ,name='master_sub' ),

    #### for master Book ########

    url(r'^master_book/$',Master_book ,name='master_book' ),
    url(r'^master_book/(?P<bid>[0-9]+)/$',Master_book_details ,name='master_book_detail' ),

    #### for master Bus ########

    url(r'^master_bus/$',Master_bus ,name='master_bus' ),
    url(r'^master_asign_bus/$',Master_asign_bus ,name='master_asign_bus' ),
    url(r'^master_driver/$',Master_driver ,name='master_driver' ),
    url(r'^master_driver/(?P<opt>[\w-]+)/$',Master_add_driver ,name='master_add_driver' ),

    #### for master Route ########

    url(r'^master_bus_rou te/$',Master_route ,name='master_route' ),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
