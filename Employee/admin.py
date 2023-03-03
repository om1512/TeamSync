from django.contrib import admin
from .models import Employee,Employee_performance,emp_task
# Register your models here.

admin.site.register(Employee)
admin.site.register(Employee_performance)
admin.site.register(emp_task)