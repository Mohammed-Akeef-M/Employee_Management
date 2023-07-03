from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    isActive = True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True  
             

    print("this function is called from views")
    date = datetime.datetime.now()
    
    name='Mohammed Akeef M'
    list_of_programs = [
        'WAP to check leap year \n',
        'WAP to check prime no \n',
        'WAP to multiple numbers \n',
        'WAP to add numbers'
    ]
    student = {
        'name':'RAhul',
        'class':10,
        'college':'VVCE',
        'city':'delhi'
    }
    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student':student

    }
    #return HttpResponse("<h1> this is index page</h1>" + str(date))
    return render(request,"home.html",data)


def about(request):
    #return HttpResponse("<h1> this is about page </h1>")
    return render(request,"about.html",{})

    
def services(request):
    #return HttpResponse("<h1> this is services page </h1>")
    return render(request,"services.html",{})