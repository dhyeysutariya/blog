from django.shortcuts import render
from assignments.models import About, SocialLink
from blogs.models import Blog, Category
def home(request):
    featured_blogs=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    blogs=Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    try:
        about=About.objects.get()
    except:
        about=None
    data={
        'featured_blogs':featured_blogs,
        'blogs':blogs,
        'about':about,
    }
    print(featured_blogs)
    return render(request,'home.html',data) 