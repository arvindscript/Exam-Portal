from django.shortcuts import render, HttpResponse
from Portal_App.forms import Signup
from django.contrib.auth.models import User
# from Portal_App.models import *
# Create your views here.
def INDEX(request):
    # stu=Candidate.objects.all() 
    return render(request,'index.html')
    
def CREATE (request):
    if request.method=='POST':
        signupform=Signup(request.POST)
        if signupform.is_valid() and signupform.cleaned_data['password']==signupform.cleaned_data['confirm_password']:
            password=signupform.cleaned_data['password']
            fname=signupform.cleaned_data['first_name']
            lname=signupform.cleaned_data['last_name']
            email=signupform.cleaned_data['email']
            username=signupform.cleaned_data['username']

            new_user = User.objects.create_user(username, email, password)
            new_user.first_name=fname
            new_user.last_name=lname
            new_user.save()
        else:
            print('password is match')
    signupform = Signup()
    context={
        'signupform':signupform
    }
    return render(request,'test.html', context)   



