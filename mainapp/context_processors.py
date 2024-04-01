from .models import Packages,Testimonials,Blogs


def package(req):
    links=Packages.objects.all()
   
    return dict(package=links)

def testimonials(req):
    testimonials=Testimonials.objects.all()
    return ({"testimonials":testimonials})
def blogs(req):
    blog=Blogs.objects.all()
    return ({"blog":blog})