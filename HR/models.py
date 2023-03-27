from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HR(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='HR/image')
    joining_date = models.DateField()
    department = models.CharField(max_length=100,default='HR')
    position = models.CharField(max_length=100)
    role = models.CharField(max_length=100,default='Management')
    working_desk = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    email_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    resident_address = models.CharField(max_length=150)
    hometown = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user_name)
    
    
class vacancy(models.Model):
    vacancy_id = models.BigAutoField(primary_key=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    main_work = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    number_of_vacancy = models.IntegerField()
    status = models.CharField(default='Open',max_length=50)
    requirement = models.CharField(max_length=200,default='')
    def __str__(self):
        return str(self.vacancy_id)
    
class appliers(models.Model):
    vacancy_id = models.ForeignKey(vacancy,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    cv = models.FileField(upload_to='Applier/CV')
    status = models.CharField(max_length=20,default='')
    
    def __str__(self):
        return str(self.vacancy_id)
    
class salaryHistory(models.Model):
    salary_id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    amount = models.IntegerField()
    def __str__(self):
        return str(self.salary_id)
    

