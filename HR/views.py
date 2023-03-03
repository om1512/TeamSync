import datetime
import time
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Employee.models import Employee,Employee_performance,emp_task
from HR.models import HR
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

# Create your models here.
# Create your views here.


def performance(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        employees = Employee.objects.all()

        return render(request, 'HR/performance.html',{'firstname':hr.first_name,'image':image,'employees':employees,'n':1})
    else:
        return redirect('/')


def payroll(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        return render(request, 'HR/payroll.html',{'firstname':hr.first_name,'image':image})
    else:
        return redirect('/')


def recruitment(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        return render(request, 'HR/recruitment.html',{'firstname':hr.first_name,'image':image})
    else:
        return redirect('/')


def leaveNotes(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        return render(request, 'HR/leavenotes.html',{'firstname':hr.first_name,'image':image})
    else:
        return redirect('/')


def addEmployee(request):

    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('password') and request.POST.get('confirmpassword') and request.FILES.get('profile') and request.POST.get('mobileno') and request.POST.get('email') and request.POST.get('surname') and request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('joiningdate') and request.POST.get('department') and request.POST.get('position') and request.POST.get('role') and request.POST.get('supervisor') and request.POST.get('workingdesk') and request.POST.get('address') and request.POST.get('hometown') and request.POST.get('gender') and request.POST.get('salary'):
                if request.POST.get('password') == request.POST.get('confirmpassword'):
                    emp = Employee()
                    user = User()
                    try:
                        user.username = request.POST.get('username')
                        user.set_password(request.POST.get('password'))
                        user.is_superuser = False
                        user.save()
                        try:
                            emp.user_name = User.objects.get(username=request.POST.get('username'))
                            emp.surname = request.POST.get('surname')
                            emp.first_name = request.POST.get('firstname')
                            emp.last_name = request.POST.get('lastname')
                            emp.joining_date = request.POST.get('joiningdate')
                            emp.department = request.POST.get('department')
                            emp.position = request.POST.get('position')
                            emp.mobile_no = request.POST.get('mobileno')
                            emp.email_id = request.POST.get('email')
                            emp.role = request.POST.get('role')
                            emp.supervisor = request.POST.get('supervisor')
                            emp.working_desk = request.POST.get('workingdesk')
                            emp.resident_address = request.POST.get('address')
                            emp.hometown = request.POST.get('hometown')
                            emp.profile_picture = request.FILES.get('profile')
                            emp.gender = request.POST.get('gender')
                            emp.date_of_birth = request.POST.get('dob')
                            emp.salary = request.POST.get('salary')
                            emp.save()
                            print('inserted')
                        except Exception as e:
                            messages.error(request, 'Something Went Wrong Here')
                    except Exception as e:
                        messages.error(request, 'User Already Exist')
                    messages.success(
                        request, 'Employee Data Inserted Successfully')
                else:
                    messages.error(request, 'Mismatch Passwords Fields')
            else:
                messages.error(request, 'Please Fill All Fields')
            return render(request, 'HR/addemployee.html',{'firstname':hr.first_name,'image':image})
        else:
            return render(request, 'HR/addemployee.html',{'firstname':hr.first_name,'image':image})
    else:
        return redirect('/')

def addTask(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        employee = Employee.objects.all()
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('task') and request.POST.get('description'):
                e_task = emp_task()
                e_task.user_name = User.objects.get(username=request.POST.get('username'))
                e_task.task = request.POST.get('task')
                e_task.description = request.POST.get('description')
                e_task.assigned_time = datetime.datetime.now()
                e_task.complete_time = datetime.datetime.now()
                e_task.save()
                messages.success(request, 'Task Added Successfully')
        return render(request, 'HR/addTask.html',{'firstname':hr.first_name,'image':image,'employee':employee})
    else:
        return redirect('/')

def addPerformance(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        user_name = request.POST.get('username')
        employee_task = emp_task.objects.filter(user_name = User.objects.get(username=user_name))       
        return render(request, 'HR/addPerformance.html',{'firstname':hr.first_name,'image':image,'employee_task':employee_task})
    else:
        return redirect('/')    


def evaluate(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        task = request.POST.get('taskid')
        print(task)
        employee_task_data = emp_task.objects.filter(task_id = task)
        if request.method == 'POST':
            if request.POST.get('taskid') and request.POST.get('hr_feedback') and request.POST.get('hr_status'):
                task_obj = emp_task.objects.get(task_id=request.POST.get('taskid'))
                task_obj.hr_feedback= request.POST.get('hr_feedback')
                if request.POST.get('hr_status') == 'Complete':
                    task_obj.complete_time = datetime.datetime.now()
                    task_obj.save()
                    first_time = task_obj.complete_time 
                    second_time = task_obj.assigned_time
                    print(first_time)
                    print(second_time)
                    # difference = first_time - second_time
                    # datetime.timedelta(0, 8, 562000)
                    # seconds_in_day = 24 * 60 * 60
                    # print("IS It Working ? ",divmod(difference.days * seconds_in_day + difference.seconds, 60))
                    task_obj.employee_status = 'Complete'
                    task_obj.hr_status = request.POST.get('hr_status')
                task_obj.save()
                task_obj.save()
        return render(request, 'HR/evaluate.html',{'firstname':hr.first_name,'image':image,'task_data':employee_task_data})
    
    else:
        return redirect('/')

def logout(request):
    auth_logout(request)
    redirect('/')




        