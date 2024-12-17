from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib import messages
import os
# import difflib

# Create your views here.

def sreg(request):
    if request.method=="POST":
        sname = request.POST.get("sname")
        semail = request.POST.get("semail")
        password = request.POST.get("Password")
        c_password = request.POST.get("C_password")
        sImage = request.FILES.get("sImage")
        sloc = request.POST.get("sloc")
        saddress = request.POST.get("saddress")
        sPh = request.POST.get("sPh")
        syear = request.POST.get("syear")
        if password==c_password:
            if Sever_Reg.objects.filter(semail=semail).exists():
                messages.info(request,'Email already exists')
            else:
                data = Sever_Reg(sname=sname, semail=semail, password=password, sImage=sImage, sloc=sloc, saddress=saddress, sPh=sPh, syear=syear)
                data.save()
                return redirect("slog")   
        else:
            messages.info(request, 'Passwords do not match')
    return render(request,'service/sever_reg.html')

def slog(request):
    if request.method=="POST":
        try:
            semail=request.POST.get('semail')
            password=request.POST.get('Password')
            # username=request.POST.get('Name')
            logdata=Sever_Reg.objects.get(semail=semail, password=password)
            request.session['semail']=logdata.semail
            request.session['id']=logdata.id
            return redirect('shome')
        except Sever_Reg.DoesNotExist as e:
            messages.info(request,'Incorrect password or email')
    return render(request,'service/slogin.html')


def shome(request):
    
    return render(request, 'service/shome.html')


def seditprofile(request):
    e = Sever_Reg.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            e.Image = request.POST.get("Images")
            e.name = request.POST.get("Name")
            e.email = request.POST.get("Email")
            e.password = request.POST.get("Password")
            e.save()
  

    return render(request, 'seditprofile.html',{'e':e})