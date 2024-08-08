from django.shortcuts import render,redirect
from .models import Register
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.method=="POST":
       username=request.POST["uname"]
       password=request.POST["password"] 
       user = Register.objects.filter(username=username,password=password).first()
       if user is None:
           messages.error(request,'inavalid Password')
           return redirect('signin')
       else:
           request.session['uname']=username
           return redirect('home')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        username=request.POST["uname"]
        password=request.POST["password"]
        myreg=Register(name=name,phone=phone,email=email,username=username,password=password)
        myreg.save()
        return redirect('signin')
    return render(request,'register.html')  
def index(request):
    return render(request,"indexnew.html")
def logout(request):
    if 'uname' in request.session:
        request.session.flush()
        return redirect('signin')
def viewall(request):
        if 'uname' not  in request.session:
            return redirect('signin')
        reg=Register.objects.aal()
        context={
            'reg':reg,
        }
        return render(request,"viewreg.html",context)
def updatereg(request,pk):
        pass





