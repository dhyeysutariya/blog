from django.shortcuts import render
from blogs.models import Blog, Category
def home(request):
    featured_blogs=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    blogs=Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    data={
        'featured_blogs':featured_blogs,
        'blogs':blogs
    }
    print(featured_blogs)
    return render(request,'home.html',data) 