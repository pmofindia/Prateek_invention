from django.db import models

class Master_course_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=20, null=True)
    medium = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name + '/' + self.medium

class Master_fee_type_data(models.Model):

    name = models.CharField(max_length=100,null=True)

    created_date = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Master_fee_packege_data(models.Model):
    course = models.ForeignKey(Master_course_data,models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    one_time = models.BooleanField(default=False)
    discount_for_single = models.CharField(max_length=100,null=True)
    discount_group_2_5 = models.CharField(max_length=100,null=True)
    discount_group_6_11 = models.CharField(max_length=100, null=True)
    discount_group_11_20 = models.CharField(max_length=100, null=True)
    discount_group_more_20 = models.CharField(max_length=100, null=True)
    installment = models.BooleanField(default=False)
    i_discount_for_single = models.CharField(max_length=100, null=True)
    i_discount_group_2_5 = models.CharField(max_length=100, null=True)
    i_discount_group_6_11 = models.CharField(max_length=100, null=True)
    i_discount_group_11_20 = models.CharField(max_length=100, null=True)
    i_discount_group_more_20 = models.CharField(max_length=100, null=True)
    monthly_install = models.BooleanField(default=False)
    m_discount_for_single = models.CharField(max_length=100, null=True)
    m_discount_group_2_5 = models.CharField(max_length=100, null=True)
    m_discount_group_6_11 = models.CharField(max_length=100, null=True)
    m_discount_group_11_20 = models.CharField(max_length=100, null=True)
    m_discount_group_more_20 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Master_make_installment(models.Model):
    packege = models.ForeignKey(Master_fee_packege_data, models.CASCADE, null=True)
    installment_1 = models.CharField(max_length=100, null=True)
    installment_2 = models.CharField(max_length=100, null=True)
    installment_3 = models.CharField(max_length=100, null=True)
    installment_4 = models.CharField(max_length=100, null=True)
    installment_5 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.packege

class Master_monthly_installment(models.Model):
    packege = models.ForeignKey(Master_fee_packege_data, models.CASCADE, null=True)
    no_of_month = models.CharField(max_length=100, null=True)
    month = models.CharField(max_length=100,null=True)
    fee = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.packege


class Master_fee_type_packege_data(models.Model):
    course = models.ForeignKey(Master_fee_packege_data, models.CASCADE, null=True)

    fee_type = models.CharField(max_length=100, null=True)
    fee = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.course.name + '---' + self.fee_type


class Master_subject_data(models.Model):

    course = models.ForeignKey(Master_course_data,models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name + '-' + self.course.name + '/' + self.course.medium



class Master_medium_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name

class Master_catbook_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name

class Master_subcatbook_data(models.Model):
    category = models.ForeignKey(Master_catbook_data,models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name

class Master_book_data(models.Model):
    category = models.ForeignKey(Master_catbook_data,models.CASCADE,null=True)
    subcategory = models.ForeignKey(Master_subcatbook_data,models.CASCADE,null=True)
    book_title = models.CharField(max_length=100, null=True)
    subbook_title = models.CharField(max_length=100, null=True)
    ISBN = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    publisher = models.CharField(max_length=100, null=True)
    editor = models.CharField(max_length=100, null=True)
    series = models.CharField(max_length=100, null=True)
    publication_year = models.CharField(max_length=100, null=True)
    edition = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    pages = models.CharField(max_length=100, null=True)
    copies = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.book_title + '-' + self.category.name + '(category)'

class Master_E_Book(models.Model):
    category = models.ForeignKey(Master_catbook_data, models.CASCADE, null=True)
    subcategory = models.ForeignKey(Master_subcatbook_data, models.CASCADE, null=True)
    book_title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    publisher = models.CharField(max_length=100, null=True)
    book = models.FileField(null=True)
    created_date = models.CharField(max_length=100, null=True)






class Master_batch_data(models.Model):
    course = models.ForeignKey(Master_course_data, models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    start_time =models.TimeField(max_length=100, null=True)
    end_time = models.TimeField(max_length=100, null=True)
    start_date =models.CharField(max_length=100, null=True)
    end_date = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name + ' - '+ self.course.name + ' course '




class Register_Student(models.Model):
    course = models.ForeignKey(Master_course_data, on_delete=models.CASCADE)
    batch = models.ForeignKey(Master_batch_data, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    roll_num = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Library_Issue_Book(models.Model):
    book = models.ForeignKey(Master_book_data, on_delete=models.CASCADE)
    student = models.ForeignKey(Register_Student, on_delete=models.CASCADE)
    issue = models.CharField(max_length=50, null=True, blank=True)
    Due = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    Return = models.CharField(max_length=50, null=True, blank=True)
    late_fee = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.student.name + " / " + self.book.book_title




class LateFine(models.Model):
    libraryfine = models.CharField(max_length=20, null=True, blank=True)
    latefeefine = models.CharField(max_length=20, null=True, blank=True)

class Master_holiday_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    start_date =models.CharField(max_length=100, null=True)
    end_date = models.CharField(max_length=100, null=True)
    reason = models.TextField(max_length=1500,null=True)
    created_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Master_designation_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name




class Master_employee_data(models.Model):
    image = models.FileField(null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, null=True)
    quali_year = models.CharField(max_length=100, null=True)
    exp_year = models.CharField(max_length=100, null=True)
    discription_exp = models.TextField(max_length=1000, null=True)
    address = models.TextField(max_length=500, null=True)
    dob = models.CharField(max_length=100, null=True)
    aadhar_card = models.CharField(max_length=13, null=True)
    join_date = models.DateField(max_length=13, null=True)
    office_in_time = models.TimeField(max_length=13, null=True)
    office_out_time = models.TimeField(max_length=13, null=True)
    finger_registration = models.FileField( null=True)
    resume = models.FileField(null=True)

    created_date = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name + '-' + self.designation

class Master_paymentmode_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Master_area_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Master_bus_data(models.Model):
    name = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name + ' - ' + self.number

class Master_driver_data(models.Model):
    image = models.FileField(null=True)
    name = models.CharField(max_length=100, null=True)
    license_number = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name + ' - ' + self.license_number


class Master_route_data(models.Model):
    area = models.ForeignKey(Master_area_data, models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    time = models.TimeField(max_length=100, null=True)
    asign = models.BooleanField(default=False)
    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name + ' - ' + self.area.name


class Master_asign_bus_data(models.Model):
    bus = models.ForeignKey(Master_bus_data, models.CASCADE, null=True)
    driver = models.ForeignKey(Master_driver_data, models.CASCADE, null=True)
    area = models.ForeignKey(Master_area_data, models.CASCADE, null=True)

    created_date = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.bus.name + ' - ' + self.driver.name

