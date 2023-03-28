from django.contrib import admin
from .models import Employee,emp_task,leaves,attendance,employee_salary_history
# Register your models here.

admin.site.register(Employee)
admin.site.register(emp_task)
admin.site.register(leaves)
admin.site.register(attendance)
admin.site.register(employee_salary_history)