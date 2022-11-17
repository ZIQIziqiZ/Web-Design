from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http.response import JsonResponse
from django.db.models import Count
import json
from student.models import Student
# Create your views here.

def WebIndex(request):
    return render(request, 'WebIndex.html')

def Accounting(request):
    return render(request, 'Accounting.html')

def Finance(request):
    return render(request, 'Finance.html')

def Language(request):
    return render(request, 'Language.html')

def InsAccounting(request):
    return render(request, 'Ins-Accounting.html')

def InsFinance(request):
    return render(request, 'Ins-Finance.html')

def InsLanguage(request):
    return render(request, 'Ins-Language.html')

def Class(request):
    return render(request, 'class.html')

def Profile(request,stu_name):
    stu_info = Student.objects.get(name=stu_name)
    return render(request, 'profile.html', {"student_info": stu_info})

def EditProfile(request,stu_name):
    if request.method == "POST":
        stu_gender = request.POST.get("editgender")
        stu_phone = request.POST.get("editphone")
        Student.objects.filter(name=stu_name).update(gender=stu_gender,phone=stu_phone)
        stu_info = Student.objects.get(name=stu_name)
        return render(request, 'editprofile.html', {"student_info": stu_info})
    stu_info = Student.objects.get(name=stu_name)
    return render(request, 'editprofile.html', {"student_info": stu_info})
    