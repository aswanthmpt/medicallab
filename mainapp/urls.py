from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('tests/',views.tests,name='tests'),
    path('packages/',views.packages,name='packages'),
    path('ourpackages/<int:id>',views.ourpackages,name='ourpackages'),
    path('blog/',views.blog,name='blog'),
    path('blogdetails/<int:id>',views.blogdetails,name='blogdetails'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('privacy/',views.privacy,name='privacy'),
    path('gallery/',views.gallery,name='gallery'),
    path('branches/',views.branches,name='branches'),
    path('branchdetails/<int:id>',views.branchdetails,name='branchdetails'),
    path('contact/',views.contact,name='contact'),
    path('departments/',views.departments,name='departments'),
    path('makeappointment/',views.makeappointment,name='makeappointment'),
]
