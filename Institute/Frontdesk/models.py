from django.db import models
from Institute.models import *
from django.forms import ModelForm

COLOR_CHOICES = (
    ('','Gender'),
    ('male','Male'),
    ('female', 'Female'),

)
class Front_student_data(models.Model):


    ##### Course Details ########
    course = models.ForeignKey(Master_course_data,models.CASCADE, null=True,
                              default='' )
    Batch = models.ForeignKey(Master_batch_data,models.CASCADE, null=True,default='')


    ##### Basic Details #######

    name = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=20, null=True)
    address = models.TextField(max_length=500, null=True)
    mobile = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=100, null=True)
    college = models.CharField(max_length=100, null=True)
    graduation = models.CharField(max_length=100, null=True)
    stream = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10,choices=COLOR_CHOICES,default='Gender')
    #### Parents Details #########
    Father_name = models.CharField(max_length=100, null=True)
    father_mob = models.CharField(max_length=13, null=True)
    Occupation = models.CharField(max_length=100, null=True)
    father_add = models.CharField(max_length=200, null=True)
    ##### Fee Details #######
    discount = models.CharField(max_length=100, null=True)
    total_fee = models.CharField(max_length=100, null=True)
    first_installment = models.CharField(max_length=100, null=True)
    second_installment = models.CharField(max_length=100, null=True)
    install_last_date = models.CharField(max_length=100, null=True)
    addmission_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name + ' -- ' + self.course.name

class Front_enquiry_data(models.Model):
    course = models.ForeignKey(Master_course_data,models.CASCADE,null=True ,default='')
    student_name = models.CharField(max_length=100,null=True)
    father_name = models.CharField(max_length=100,null=True)
    college = models.CharField(max_length=100,null=True)
    graduation = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=13,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    follow_up_date = models.CharField(max_length=100,null=True)
    follow_up_time = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=500,null=True)
    visited_date = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.student_name + ' -- ' + self.course.name












