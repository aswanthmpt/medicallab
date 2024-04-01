from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone=models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
   
    def __str__(self):
        return self.name
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    address=models.TextField()
    message = models.TextField()
   
    def __str__(self):
        return self.name
    
class Packages(models.Model):
    name=models.CharField(max_length=250,unique=True)
    image=models.ImageField(upload_to='package')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    tests=models.TextField(blank=True, null=True)
    note=models.CharField(max_length=250, blank=True, null=True)
    homecollection=models.TextField(blank=True,null=True)
    class Meta:
        ordering=('name',)
        verbose_name='package'
        verbose_name_plural='packages'
    def __str__(self):
        return self.name
class Blogs(models.Model):
    
    image=models.ImageField(upload_to='blog')
    date=models.DateField()
    h1=models.TextField(blank=True,null=True)
    p1=models.TextField(blank=True, null=True)
    h2=models.TextField(blank=True,null=True)
    p2=models.TextField(blank=True, null=True)
    h3=models.TextField(blank=True,null=True)
    p3=models.TextField(blank=True, null=True)
    h4=models.TextField(blank=True,null=True)
    p4=models.TextField(blank=True, null=True)
    h5=models.TextField(blank=True,null=True)
    p5=models.TextField(blank=True, null=True)
    h6=models.TextField(blank=True,null=True)
    p6=models.TextField(blank=True, null=True)
    h7=models.TextField(blank=True,null=True)
    p7=models.TextField(blank=True, null=True)
    r1=models.TextField(blank=True, null=True)
    r2=models.TextField(blank=True, null=True)
   
    class Meta:
        ordering=('h1',)
        verbose_name='blog'
        verbose_name_plural='blogs'
    def __str__(self):
        return self.h1
    
class Gallery(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='gallery')
    class Meta:
        verbose_name='gallery'
    def __str__(self):
        return self.name
class Branches(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField()
    map=models.TextField()
    image=models.ImageField(upload_to='branches')
    image2=models.ImageField(upload_to='branches')
    class Meta:
        verbose_name='branches'
    def __str__(self):
        return self.name
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    review=models.TextField()
    class Meta:
        verbose_name='testimonials'
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.TextField()
    
   
    def __str__(self):
        return self.name