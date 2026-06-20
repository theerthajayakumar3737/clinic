from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def appointment(request):
    if request.method== 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Allappointments')
    else:
        form = AppointmentForm()            

    return render(request,"appointment.html",{"form":form})



def delete_appnt(request , id):

        appnts =Appointments.objects.get(id = id)
        appnts.delete()
        return redirect('/Allappointments')
    
    
def update_appnt(request ,id):
    appnts =Appointments.objects.get(id = id)
    if request.method == "POST":
        form = AppointmentForm(request.POST,instance=appnts)
        if form.is_valid():
            form.save()
            return redirect('/Allappointments')
    else:
        form = AppointmentForm(instance=appnts)
    return render(request,'Update_appointment.html',{"form":form})






def allappoint(request):
    if request.method== "GET":
        appnts = Appointments.objects.all()
    return render(request , 'Allappointments.html',{"appointments":appnts})
    


def contact(request):
    return render(request , 'contact.html')

def about(request):
    return render(request,"about.html")

def departments(request):
    return render(request,"departments.html")

def services(request):
    return render(request,"services.html")

def doctors(request):
    return render (request,"doctors.html")
