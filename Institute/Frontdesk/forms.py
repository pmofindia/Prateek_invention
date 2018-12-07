
from .models import *
from django import forms
from datetime import date,datetime
class Student_form(forms.ModelForm):

    class Meta:
        model = Front_student_data

        exclude = ('updated', 'created')
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name', 'name': 'Name',
                                           'class': 'form-control',
                                           "required":''}),
            "dob": forms.TextInput(attrs={'placeholder': 'Date of Birth', 'name': 'dob',
                                           'class': 'form-control'
                                          ,"required":''
                                          }),
            "address": forms.TextInput(attrs={'placeholder': 'Address', 'name': 'address',
                                          'class': 'form-control'
                                              ,"required":''}),
            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile Number', 'name': 'mob',
                                          'class': 'form-control',
                                             "required": ''}),
            "email": forms.TextInput(attrs={'placeholder': 'Email Address', 'name': 'email',
                                          'class': 'form-control',
                                            "required": ''}),
            "college": forms.TextInput(attrs={'placeholder': 'College/School', 'name': 'college',
                                          'class': 'form-control',
                                              "required": ''}),
            "graduation": forms.TextInput(attrs={'placeholder': 'Graduation/Standard', 'name': 'graduation',
                                          'class': 'form-control',
                                                 "required": ''  }),

            "gender": forms.Select(attrs={'name': 'gender',
                                     'class': 'form-control show-tick',
                                          "required": ''
                                     }),
            "stream": forms.TextInput(attrs={'placeholder': 'Stream/Subject', 'name': 'stream',
                                                 'class': 'form-control',
                                             "required": ''
                                                 }),
            "Father_name": forms.TextInput(attrs={'placeholder': 'Father\'s name', 'name': 'father',
                                             'class': 'form-control',
                                                  "required": ''
                                             }),
            "father_mob": forms.TextInput(attrs={'placeholder': 'Father\'s Contact No.', 'name': 'father_mob',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "father_add": forms.TextInput(attrs={'placeholder': 'Father\'s Address', 'name': 'father_add',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "Occupation": forms.TextInput(attrs={'placeholder': 'Father\'s Occupation', 'name': 'occupation',
                                                  'class': 'form-control',
                                                 "required": ''
                                                  }),
            "discount": forms.TextInput(attrs={'placeholder': 'Discount', 'name': 'discount',
                                                 'class': 'form-control',
                                               'id':'Text1',
                                               'onkeyup':'add_number()',
                                                "required":''
                                                 }),
            "total_fee": forms.TextInput(attrs={'placeholder': 'Total Fee', 'name': 'total_fee',
                                               'class': 'form-control',
                                               'id':'txtresult',
                                                "required":''
                                               }),
        }



class Enquiry_form(forms.ModelForm):
    class Meta:
        model = Front_enquiry_data
        today_date = date.today()
        format_date = datetime.strptime(str(today_date), "%Y-%m-%d").strftime('%d/%m/%Y')
        exclude = ()
        widgets = {
            "student_name": forms.TextInput(attrs={'placeholder': 'Name',
                                           'class': 'form-control',"required":'1'}),
            "father_name": forms.TextInput(attrs={'placeholder': 'Fathers\'name',
                                                   'class': 'form-control', "required": '1'}),

            "address": forms.TextInput(attrs={'placeholder': 'Address',
                                              'class': 'form-control',"required":'1'}),

            "mobile": forms.TextInput(attrs={'placeholder': 'Mobile Number',
                                             'class': 'form-control',"required":'1'}),

            "email": forms.EmailInput(attrs={'placeholder': 'Email Address',
                                            'class': 'form-control',"required":'1'}),

            "college": forms.TextInput(attrs={'placeholder': 'College/School',
                                              'class': 'form-control',"required":'1'}),

            "graduation": forms.TextInput(attrs={'placeholder': 'Graduation/Standard',
                                                 'class': 'form-control',"required":'1'
                                                 }),

            "course": forms.Select(attrs={'class': 'form-control show-tick',"required":'1',
                                          'id':'course.value'}),

            "remark": forms.TextInput(attrs={'placeholder': 'Remark',
                                             'class': 'form-control',"required":'1'
                                             }),

            "follow_up_date": forms.TextInput(attrs={'placeholder': 'Follow Up Date',
                                                  'class': 'form-control',"required":'1'
                                                  }),
            "follow_up_time": forms.TextInput(attrs={'placeholder': 'Follow Up Time',
                                                     'class': 'form-control', "required": '1'
                                                     }),
            "visited_date": forms.TextInput(attrs={'class': 'form-control', "required": '',
                                                   'value':format_date,
                                                   'readonly':''})
    }

