from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

# Create your views here.

def profile(request):
    return render(request,'Employee/profile.html')

def request_leaves(request):
    return render(request,'Employee/request_leaves.html')

def projects(request):
    return render(request,'Employee/projects.html')

def query(request):
    return render(request,'Employee/query.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
