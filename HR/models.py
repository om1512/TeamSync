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