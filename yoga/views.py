from django.shortcuts import render
from django.http import HttpResponse
from app.models import contact, contactus, subscribe


def homePage(request):

    try:

        if request.method=="POST":
            email=request.POST.get("email")
            data=subscribe(email=email)
            data.save()
    except:
        pass

    return render(request,"index.html")

def about(request):
   

    return render(request,"about.html")



def join(request):
    try:

        if request.method=="POST":
            name=request.POST.get("name")
            username=request.POST.get("username")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            password=request.POST.get("password")
            password1=request.POST.get("password1")
            gender=request.POST.get("gender")
            data=contact(name = name,username=username,email=email, phone=phone, password=password,password1=password1,gender=gender)
            data.save()
    except:
        pass
    return render(request,"join.html")

def contactUs(request):
    try:

        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            message=request.POST.get("message")
            data=contactus(name = name,email=email,message=message)
            data.save()
    except:
        pass
    return render(request,"contactUs.html")
