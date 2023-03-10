from django.contrib import admin
from .models import Employee,emp_task,leave_notes
# Register your models here.

admin.site.register(Employee)
admin.site.register(emp_task)
admin.site.register(leave_notes)
