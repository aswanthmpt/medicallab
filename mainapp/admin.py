from django.contrib import admin
from . models import Packages,Gallery,Testimonials,Enquiry,Contact,Appointment,Blogs,Branches

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Contact)
admin.site.register(Appointment)
class PackagesAdmin(admin.ModelAdmin):
 
    list_display=['name','image','price','note','homecollection']
    list_editable=['image','price','note','homecollection']
admin.site.register(Packages,PackagesAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display=['name','image','map']
    list_editable=['image','map']
admin.site.register(Branches,BranchAdmin)

class GalleryAdmin(admin.ModelAdmin):
 
    list_display=['name','image']
    list_editable=['image']
admin.site.register(Gallery,GalleryAdmin)

class TestimonialsAdmin(admin.ModelAdmin):
    list_display=['name','place']
admin.site.register(Testimonials,TestimonialsAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display=['h1']
admin.site.register(Blogs,BlogsAdmin)