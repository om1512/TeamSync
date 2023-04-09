import datetime
import time
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Employee.models import Employee,emp_task,leaves,employee_salary_history
from HR.models import vacancy,appliers,salaryHistory
from HR.models import HR
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.utils import timezone
from django.core.mail import send_mail
from django.db import connection
from django.forms import formset_factory
from django.views.decorators.csrf import csrf_exempt
import razorpay
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

@csrf_exempt
def success(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('salary'):
            s = employee_salary_history()
            s.user_name = User.objects.get(username = request.POST.get('name')) 
            da = datetime.date.today()
            s.year = da.year
            s.month = da.month
            s.salary = request.POST.get('salary')
            s.save()
    return render(request, "HR/payroll.html")

def payroll(request):
    if request.user.is_authenticated:
        sh = salaryHistory()
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        salary_history = salaryHistory.objects.all()
        sal = Employee.objects.all()
        totalSum = 0
        for e in sal:
            totalSum += e.salary
        date = datetime.date.today()
        statusUpdate(date.month,date.year)
        s = salaryHistory.objects.filter(year = date.year,month = date.month)  
        if len(s) == 0:
            stat = "false"
        else:
            stat = "true"
            sh.year = date.year
            sh.month = date.month
            sh.amount = totalSum
            sh.save()

        if request.method == "POST":
            name = request.POST.get('name')
            amount = 10000

            client = razorpay.Client(
                auth=("rzp_test_ULKXFl3prtGM7z", "IQyDNCHgqTTcZj1SGroTb0Cl"))

            payment = client.order.create({'amount': 100, 'currency': 'INR',
                                        'payment_capture': '1'})
        return render(request, 'HR/payroll.html',{'firstname':hr.first_name,'image':image,'salaryHistory':salary_history,'sal':sal,'month':date.month,'year':date.year,'stat':stat,'amount':100})
    else:
        return redirect('/')

def leaveResponse(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        l = leaves.objects.all()
        if request.POST.get('username') and request.POST.get('response') and request.POST.get('submit'):    
                ll = leaves.objects.get(leave_id=request.POST.get('username'))
                ll.response=request.POST.get('response')
                ll.status=request.POST.get('submit')
                ll.save()
        return render(request, 'HR/leaveResponse.html',{'firstname':hr.first_name,'image':image,'leave_notes':l})
    else:
        return redirect('/')

def recruitment(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        v = vacancy.objects.all()
        a = appliers.objects.all()  
        print(a)
        if request.method == 'POST':
            if request.POST.get('vacancy_id') and request.POST.get('submit') == 'Close':
                print(request.POST.get('submit'))
                vacancy.objects.filter(vacancy_id = request.POST.get('vacancy_id')).delete()
                return render(request, 'HR/recruitment.html',{'firstname':hr.first_name,'image':image,'vacancy':v,'appliers':a})
            if request.POST.get('cv') and request.POST.get('submit') == 'View':
                return redirect('/media/'+request.POST.get("cv"))
            if request.POST.get('applier_id') and request.POST.get('submit') == 'Approve':
                appliers.objects.filter(id = request.POST.get('applier_id')).update(status = 'Approve')
                Applier = appliers.objects.get(id = request.POST.get('applier_id'))
                Vacnacy = vacancy.objects.get(vacancy_id = str(Applier.vacancy_id))
                send_mail(
                        'Job Application Latter Status',
                        'Dear, '+ Applier.name+'\nYou have Applied For '+Vacnacy.main_work+' in Department '+Vacnacy.department+'\nYou are SELECTED for this position. we will soon notify you about further procedure.\nFor Query contact us omdhingani0@gmail.com',
                        'omdhingani0@gmail.com',
                        [Applier.email],
                        fail_silently=False,)   
                return render(request, 'HR/recruitment.html',{'firstname':hr.first_name,'image':image,'vacancy':v,'appliers':a})
            if request.POST.get('applier_id') and request.POST.get('submit') == 'Reject':
                appliers.objects.filter(id = request.POST.get('applier_id')).update(status = 'Reject')
                Applier = appliers.objects.get(id = request.POST.get('applier_id'))
                Vacnacy = vacancy.objects.get(vacancy_id = str(Applier.vacancy_id))
                send_mail(
                        'Job Application Latter Status',
                        'Dear, '+ Applier.name+'\nYou have Applied For '+Vacnacy.main_work+' in Department '+Vacnacy.department+'\nYou are NOT SELECTED for this position.\nWish you ALL THE BEST for your upcoming future. KEEP TRYING & KEEP GROWING\nFor Query contact us on omdhingani0@gmail.com',
                        'Om Dhingani',
                        [Applier.email],
                        fail_silently=False,)  
                return render(request, 'HR/recruitment.html',{'firstname':hr.first_name,'image':image,'vacancy':v,'appliers':a})
            
        return render(request, 'HR/recruitment.html',{'firstname':hr.first_name,'image':image,'vacancy':v,'appliers':a})    
    else:
        return redirect('/')    


def leaveNotes(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)
        l = leaves.objects.all()
        return render(request, 'HR/leavenotes.html',{'firstname':hr.first_name,'image':image,'leave_notes':l})
    else:
        return redirect('/')


def viewCV(request):
    cv = request.POST.get('cv')
    return redirect(request, str(cv))

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
                            print('send email to employee that he is inserted')
                            send_mail(
                        'System Login Information',
                        'Dear, '+ request.POST.get('firstname') + "\nYour UserName : "+request.POST.get('username')+"\nPassword : "+request.POST.get('password') + "\nYou Can Use This UserName and Password To Login into the System",
                        'realomdhingani@gmail.com',
                        [request.POST.get('email')],
                        fail_silently=False,)   
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
                e_task.assigned_time = timezone.localtime()
                e_task.complete_time = timezone.localtime()
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
                    task_obj.complete_time = timezone.localtime()
                    first_time = timezone.localtime()
                    second_time = task_obj.assigned_time
                    difference = first_time - second_time
                    datetime.timedelta(0, 8, 562000)
                    seconds_in_day = 24 * 60 * 60
                    p,q = divmod(difference.days * seconds_in_day + difference.seconds, 60)
                    task_obj.time_taken = (str(p)+ " min " + str(q) +" sec")
                    task_obj.employee_status = 'Complete'
                    task_obj.hr_status = request.POST.get('hr_status')
                task_obj.save()

        return render(request, 'HR/evaluate.html',{'firstname':hr.first_name,'image':image,'task_data':employee_task_data})
    
    else:
        return redirect('/')


def addVacancy(request):
    if request.user.is_authenticated:
        hr = HR.objects.get(user_name=User.objects.get(username=request.user))
        image = str(hr.profile_picture)   
        if request.method == 'POST':
            if request.POST.get('salary') and request.POST.get('vacancyNumber') and request.POST.get('department') and request.POST.get('role') and request.POST.get('Requirement'):
                v = vacancy()
                v.department = request.POST.get('department')
                v.role = request.POST.get('role')
                v.main_work =request.POST.get('work')
                v.salary_range= request.POST.get('salary')
                v.experience=request.POST.get('experience')
                v.number_of_vacancy = request.POST.get('vacancyNumber')
                v.status = 'Open'
                v.requirement = request.POST.get('Requirement')
                v.save()
                messages.success(request, 'Vacancy Released')

        return render(request, 'HR/addVacancy.html',{'firstname':hr.first_name,'image':image})
    else:
        return redirect('/') 

def logout(request):
    auth_logout(request)
    redirect('/')




def statusUpdate(m,y):
    employee = Employee.objects.all()
    for emp in employee:
        try:
            salary_history = employee_salary_history.objects.filter(user_name = User.objects.get(username = emp.user_name) ,month = 3,year = 2023)
            print(salary_history)
            if salary_history.exists():
                e = Employee.objects.get(user_name = User.objects.get(username = emp.user_name))
                e.salary_status = "Paid"
                e.save()
            else:
                e = Employee.objects.get(user_name = User.objects.get(username = emp.user_name))
                e.salary_status = "Unpaid"
                e.save()
        except Exception as e:
            print("NOT EXIST")
            e = Employee.objects.get(user_name = User.objects.get(username = emp.user_name))
            e.salary_status = "Unpaid"
            e.save()


