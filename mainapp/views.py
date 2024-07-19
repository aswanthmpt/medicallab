from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Packages,Gallery,Testimonials,Enquiry,Contact,Appointment,Blogs,Branches

# Create your views here.
def home(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        phone=req.POST.get('phone')
        email = req.POST.get('email')
        message = req.POST.get('message')
        
        enquiry = Enquiry.objects.create(name=name, email=email, message=message,phone=phone)
        enquiry.save()
        messages.info(req,'Enquiry Submitted')
        return redirect('main:home')
  
    return render(req,'index.html')
def about(req):
    
    return render(req,'aboutus.html')
def tests(req):
    
    return render(req,'tests.html')
def packages(req):
    
    return render(req,'packages.html')
def ourpackages(req,id):
    packages=Packages.objects.get(id=id)
    tests_list = packages.tests.split("\n") if packages.tests else []
    return render(req,'ourpackages.html',{"ourpackages":packages, "tests_list": tests_list})
def blog(req):
    blog=Blogs.objects.all()
    return render(req,'blog.html',{"blogs":blog})
def blogdetails(req,id):
    blog=Blogs.objects.get(id=id)
    
    return render(req,'blogdetails.html',{"blogs":blog})
def testimonials(req):
    
    return render(req,'testimonial.html')
def privacy(req):
    
    return render(req,'privacy.html')
def gallery(req):
    gallery=Gallery.objects.all()
    
    return render(req,'gallery.html',{"gallery":gallery})
def branches(req):
    branch=Branches.objects.all()
    return render(req,'branches.html',{"branches":branch})
def branchdetails(req,id):
    branches=Branches.objects.get(id=id)
    
    return render(req,'branchdetails.html',{"branches":branches})
def departments(req):
    
    return render(req,'departments.html')
def contact(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        message = req.POST.get('message')
        subject = req.POST.get('subject')
        
        contact = Contact.objects.create(name=name, email=email, message=message,subject=subject)
        contact.save()
        messages.info(req,'Contact Requested')
        return redirect('main:contact')
    
    return render(req,'contact.html')
def makeappointment(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone=req.POST.get('phone')
        date=req.POST.get('date')
        time=req.POST.get("time")
        age=req.POST.get("age")
        gender=req.POST.get("gender")
        address=req.POST.get("address")
        message = req.POST.get('message')
        
        
        appointment = Appointment.objects.create(name=name,address=address, email=email,gender=gender, message=message,phone=phone,date=date,time=time,age=age,)
        appointment.save()
        messages.info(req,'Appointment Request Submitted')
        return redirect('main:makeappointment')
    
    return render(req,'makeappointment.html')