from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import check_password
from .models import AccountVerify
from django.core.mail import EmailMessage
from users.models import MyUser
from PIL import Image

from django.contrib.auth.decorators import login_required
import os
from django.conf import settings

# Create your views here.
def index(request):
    try:
        usercount=MyUser.objects.all().count()
    except:
        usercount = 0
    return render(request, 'index.html',{'user':request.user,'alluser':usercount})

def email_send(token, email,email_message,email_subject):
    email = EmailMessage(
    email_subject,
    email_message +' '+ token,
    'python.sartia@gmail.com',
    [email],
    headers={'Message-ID': '1'},
    
)
    email.send(fail_silently=False)

def signup(request):
    print(request.method)
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST,request.FILES)
        print('pass1')
        if form.is_valid():
            email=form.cleaned_data.get('email')
            form.save()
            messages.success(request,'Please verify your email address.')
            token = get_random_string(16)
            if MyUser.objects.filter(email=email).exists():
                email=MyUser.objects.get(email=email)
                AccountVerify.objects.create(user=email, link=token)
            # token = 'http://127.0.0.1:8000/user/userverify/' + token
            token = 'http://'+str(get_current_site(request).domain)+'/accountverify/' + token
            email_send(token, email,email_message='Please click given link to verify your email ',email_subject='Registration Verification')
            return HttpResponseRedirect(reverse_lazy('firstapp:login'))
        else:
            messages.error(request,form.errors)
    return render(request, 'signup.html')

def login_view(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password1')
        print("Please",email,password)
        if email is not None and password is not None:
            print('asd')
            # user = authenticate(request, username=username, password=password)
            user = authenticate(request, email=email, password=password)
            print('user',user)
            if user is not None:
                login(request, user)
                print('login')
                response = HttpResponseRedirect(reverse_lazy('firstapp:index'))
                return response
            messages.error(request, 'Username and password is Invalid')
    return render(request, 'login.html')

def account_verify_view(request, id):
    if (AccountVerify.objects.filter(link=id).exists()):
        obj = AccountVerify.objects.get(link=id)
        obj.verify = True
        obj.save()
        obj1 = MyUser.objects.get(email=obj.user.email)
        obj1.is_active = True
        obj1.save()
        messages.success(request, 'Email verified successfully Please login')
    return redirect('firstapp:login')

@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('firstapp:login'))

@login_required(login_url='/')
def setting_profile(request):
    obj=MyUser.objects.get(id=request.user.id)
    form=UserUpdateForm(instance=obj)
    if request.method=='POST':
        obj=MyUser.objects.get(id=request.user.id)
        phone_number=request.POST.get('phone_number')
        form=UserUpdateForm(instance=obj,data=request.POST,files=request.FILES)
        if form.is_valid():
            obj=form.save()
            obj1=MyUser.objects.get(id=obj.id)
            obj1.phone_number=phone_number
            obj1.save()
            messages.success(request,'Settings updated successfully')
        else:
            messages.error(request,form.errors)
    return render(request, 'setting.html',{'user':obj,'form':form})

@login_required(login_url='/')
def change_password(request):
    obj=MyUser.objects.get(id=request.user.id)
    if request.method=='POST':
        obj=MyUser.objects.get(id=request.user.id)
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-new-password')
        if (new_password == confirm_password):
            if (check_password(password, obj.password)):
                obj.set_password(new_password)
                obj.save()
                messages.success(request,'Password Changed successfully')
            else:
                messages.error(request,'Your current password or old password not match')
        else:
            messages.error(request,'New password and Confirm password not match')
    return render(request, 'setting.html',{'user':obj})

@login_required(login_url='/')
def adduser(request):
    form=UserUpdateForm()
    if request.method == 'POST':
        form=UserUpdateForm(request.POST,request.FILES)
        password=request.POST.get('password')
        email=request.POST.get('email')
        if form.is_valid():
            obj=form.save()
            obj1=MyUser.objects.get(email=obj.email)
            obj1.set_password(password)
            obj1.save()
            messages.success(request,'User Created Successfully')
            print('saved')
        else:
            print(form.errors)
            messages.error(request,form.errors)
        
    return render(request, 'adduser.html',{'form':form})

@login_required(login_url='/')
def allusers(request):
    user=MyUser.objects.all()
    return render(request, 'allusers.html',{'allusers':user})

@login_required(login_url='/')
def edituser(request,id):
    if MyUser.objects.filter(id=id).exists():
        user=MyUser.objects.get(id=id)
        form=UserUpdateForm(instance=user)
        if request.method == 'POST':
            user=MyUser.objects.get(id=id)
            form=UserUpdateForm(instance=user,data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'User updated Successfully')
                print('saved')
                return redirect('/allusers')
            else:
                print(form.errors)
                messages.error(request,form.errors)
            return render(request, 'edituser.html',{'user':user,'form':form})
        return render(request, 'edituser.html',{'user':user,'form':form})
    else:
        messages.error(request,'User does not exist')
        return redirect('/allusers')

@login_required(login_url='/')
def deleteuser(request, id):
    if MyUser.objects.filter(id=id).exists():
        user=MyUser.objects.get(id=id)
        user.delete()
        messages.success(request,'User Deleted Successfully')
        return redirect('/allusers')
    else:
        messages.error(request,'User Not Found')
        return redirect('/allusers')

@login_required(login_url='/')
def profile(request):
    user=MyUser.objects.get(id=request.user.id)
    return render(request,'profile.html',{'user':user})