from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth

# Create your views here.


def login(request):
   if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
        
   else:
       return render(request,'login.html')
           

def register(request):
    if request.method=='POST':
         firstName = request.POST['firstName']
         lastName = request.POST['lastName']
         username = request.POST['username']
         Email = request.POST['Email']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']
         if pass1==pass2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,'Username taken')
                 return redirect('register')
             elif User.objects.filter(email=Email).exists():  
                 messages.info(request,'email taken') 
                 return redirect('register') 
             else:    
                user = User.objects.create_user(username=username,first_name=firstName,last_name=lastName,password=pass1,email=Email)
                user.save();
                print('user created')
                return redirect('login')
         else:
             messages.info(request,'password not matching')
             return redirect('register')      


    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')