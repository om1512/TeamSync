from django.contrib import admin
from .models import Employee,emp_task,leaves
# Register your models here.

admin.site.register(Employee)
admin.site.register(emp_task)
admin.site.register(leaves)
