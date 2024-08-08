from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
from .models import Doctor
from .forms import BookingForm
def index(request):
    #return render("Hello welcome")
    person={
         'name':'john',
         'age':30,
         'place':'Thrissur'
    }
    return render(request,"index.html",person)
def about(request):
    #return HttpResponse("About Us")
     return render(request,"about.html",{'range': range(1,11)})
def show(request):
    number1={
          'num':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,"show.html",number1)
def base(request):
    dic_dept = {
        'base':Department.objects.all()
    }
    return render(request,'basecall.html',dic_dept)

def Doctors(request):
    dic_doctor= {
        'doctor':Doctor.objects.all()
    }
    return render(request,'doctor.html',dic_doctor)
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form=BookingForm()
    dic_form= {
        'form':form
    }
    return render(request,'Booking.html',dic_form)



