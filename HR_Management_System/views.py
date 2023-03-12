from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from Employee.models import Employee
from HR.models import HR,vacancy,appliers
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/Add_HR')
        elif isEmployee(request.user):
            return redirect('/Employee')
        elif isHR(request.user):
            return redirect('/HR')
    else:
        if request.method == 'POST':
            user = authenticate(username=request.POST.get(
                'username'), password=request.POST.get('password'))
            print(user)
            if user is not None:
                if user.is_superuser:
                    auth_login(request, user)
                    return render(request, 'addHR.html')
                elif isEmployee(user):
                    auth_login(request, user)
                    return render(request, 'Employee/profile.html')
                elif isHR(user):
                    auth_login(request, user)
                    return render(request, 'HR/performance.html')
            else:
                messages.success(request, 'Incorrect UserName Or Password')
    return render(request, 'index.html')


def add_hr(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('confirmpassword') and request.FILES.get('profile') and request.POST.get('mobileno') and request.POST.get('email') and request.POST.get('surname') and request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('joiningdate') and request.POST.get('department') and request.POST.get('position') and request.POST.get('role') and request.POST.get('supervisor') and request.POST.get('workingdesk') and request.POST.get('address') and request.POST.get('hometown') and request.POST.get('gender') and request.POST.get('salary'):
            if request.POST.get('password') == request.POST.get('confirmpassword'):
                emp = HR()
                user = User()
                try:
                    user.username = request.POST.get('username')
                    user.set_password(request.POST.get('password'))
                    user.is_superuser = False
                    user.save()
                    try:
                        emp.user_name = User.objects.get(
                            username=request.POST.get('username'))
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
                        send_mail(
                        "Welcome to Meta",
                        'Dear, '+ request.POST.get('firstname') + "\nWe are excited to welcome you to our team."+ request.POST.get('firstname') +" will meet you in the company. Please remember this username and password. \nUserName : "+request.POST.get('username')+"\nPassword : "+request.POST.get('password') + "\n\nYou Can Use This UserName and Password To Login into Company's System",
                        '22ceuod004@ddu.ac.in',
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
        return render(request, 'addHR.html')
    else:
        return render(request, 'addHR.html')

def vacancy_info(request):
    v = vacancy.objects.all()
    return render(request, 'vacancyInfo.html',{'vacancy':v})

def isEmployee(name):
    try:
        emp = Employee.objects.get(user_name=User.objects.get(username=name))
        if emp is not None:
            return True
        else:
            return False
    except Exception as e:
        return False


def isHR(name):
    try:
        hr = HR.objects.get(user_name=User.objects.get(username=name))
        if hr is not None:
            return True
        else:
            return False
    except Exception as e:
        return False
    
def logout(request):
    auth_logout(request)
    return redirect('/')


def applyForJob(request):

        vacancy_id = request.POST.get('vacancy_id')
        print(vacancy_id)
        v = vacancy.objects.filter(vacancy_id = vacancy_id)
        if v and request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.FILES.get('cv'):
                a = appliers()
                a.vacancy_id = vacancy.objects.get(vacancy_id = vacancy_id)
                a.name = request.POST.get('name')
                a.email = request.POST.get('email')
                a.phone_no = request.POST.get('phone')
                a.cv = request.FILES.get('cv')
                a.save()
                print('inserted')
                return redirect('/vacancyInfo')
        return render(request, 'applyForJob.html',{'vacancy':v})      