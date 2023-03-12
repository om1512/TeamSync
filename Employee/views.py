from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout
from .models import Employee,emp_task,leaves
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
# Create your views here.

def profile(request):
     if request.user.is_authenticated:
        emp = Employee.objects.get(user_name=User.objects.get(username=request.user))
        image = str(emp.profile_picture)
        employee_name = request.user
        dob = emp.date_of_birth
        today = date.today()
        age= today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        Employee.objects.filter(user_name=User.objects.get(username=request.user)).update(age=age)
        profile = Employee.objects.filter(user_name=User.objects.get(username=request.user))
        user = User.objects.get(username = request.user)
        return render(request, 'Employee/profile.html',{'firstname':emp.first_name,'image':image,'employee_name':employee_name,'emp':profile})
     else:
        return redirect('/')

def request_leaves(request):
    if request.user.is_authenticated:
        emp = Employee.objects.get(user_name=User.objects.get(username=request.user))
        image = str(emp.profile_picture)
        employee_name = request.user
        print(emp.remaining_leaves)
        my_leaves = leaves.objects.filter(user_name = User.objects.get(username=request.user))
        if request.method == 'POST':
            if request.POST.get('date') and request.POST.get('days') and request.POST.get('status') and request.POST.get('purpose') and request.POST.get('description'):  
                l = leaves()
                l.user_name = User.objects.get(username=request.user)
                l.leave_from = request.POST.get('date')
                l.days = request.POST.get('days')
                l.purpose = request.POST.get('purpose')
                l.desc = request.POST.get('description')
                l.leave_type = request.POST.get('status')
                l.save()
                Employee.objects.filter(user_name=User.objects.get(username=request.user)).update(remaining_leaves=emp.remaining_leaves-1)
                messages.success(request,'Leave Note Send Successfully')
        return render(request, 'Employee/request_leaves.html',{'firstname':emp.first_name,'image':image,'employee_name':employee_name,'leaves':emp.remaining_leaves,'my_leaves':my_leaves})
    else:
        return redirect('/')

def projects(request):
     if request.user.is_authenticated:
        emp = Employee.objects.get(user_name=User.objects.get(username=request.user))
        image = str(emp.profile_picture)
        employee_name = request.user
        task = emp_task.objects.all()
        return render(request, 'Employee/projects.html',{'firstname':emp.first_name,'image':image,'employee_name':employee_name,'task':task})
     else:
        return redirect('/')


def addResponse(request):
     if request.user.is_authenticated:
        emp = Employee.objects.get(user_name=User.objects.get(username=request.user))
        image = str(emp.profile_picture)
        task_id = request.POST.get('task_id')
        task_data = emp_task.objects.filter(task_id = task_id)
        if request.method == 'POST':
            if request.POST.get('emp_feedback') and request.POST.get('emp_status') and request.POST.get('submit') and request.POST.get('taskid'):
                emp_task.objects.filter(task_id=request.POST.get('taskid')).update(employee_feedback = request.POST.get('emp_feedback'),employee_status = request.POST.get('emp_status'))
                messages.success(request, 'Response Stored Successfully')
                task_data = emp_task.objects.filter(task_id = request.POST.get('taskid'))
                return render(request, 'Employee/addResponse.html',{'firstname':emp.first_name,'image':image,'task_data':task_data})
        
        return render(request, 'Employee/addResponse.html',{'firstname':emp.first_name,'image':image,'task_data':task_data})

     else:
        return redirect('/')


def query(request):
    return render(request,'Employee/query.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
