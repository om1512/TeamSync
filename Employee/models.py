from datetime import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='Employee/image')
    joining_date = models.DateField()
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    role = models.CharField(max_length=100,default='')
    working_desk = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    email_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=20,default='male')
    date_of_birth = models.DateField()
    age = models.IntegerField(default=0)
    resident_address = models.CharField(max_length=100)
    hometown = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    remaining_leaves = models.IntegerField(default=15)
    salary_status = models.CharField(max_length=20,default="Unpaid")
    def __str__(self):
        return str(self.user_name)
    
class emp_task(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_time = models.DateTimeField()
    complete_time =  models.DateTimeField()
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    employee_feedback = models.CharField(max_length=100,default='')
    employee_status = models.CharField(max_length=20,default='')
    hr_feedback = models.CharField(max_length=100,default='')
    hr_status = models.CharField(max_length=20,default='')
    time_taken = models.CharField(max_length=70,default='')
    def __str__(self):
        return str(self.user_name)
    


class leaves(models.Model):
    leave_id = models.BigAutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    leave_type = models.CharField(max_length=20,default='')
    status = models.CharField(max_length=10)
    response = models.CharField(max_length=100,default='')
    leave_from  = models.DateField()
    days = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user_name)
    

class attendance(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=20)
    def __str__(self):
            return str(self.user_name)


class employee_salary_history(models.Model):
     user_name = models.ForeignKey(User, on_delete=models.CASCADE)
     year = models.IntegerField()
     month = models.IntegerField()
     salary = models.IntegerField(default=0)
     def __str__(self):
            return str(self.user_name)
