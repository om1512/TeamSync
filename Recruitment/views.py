from django.shortcuts import render

def vacancyInfo(request):
    return render(request, 'applier/vacancyInfo.html')
