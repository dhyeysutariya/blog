from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category

def posts_by_category(request,category_id):
    blogs=Blog.objects.filter(status='Published',category=category_id)
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category=get_object_or_404(Category,pk=category_id)
    data={
        'blogs':blogs,
        'category':category
    }
    return render(request,'posts_by_category.html',data)

def blog_by_slug(request,blog_slug):
    blog=Blog.objects.get(slug=blog_slug,status='Published')
    data={
        'blog':blog
    }
    return render(request,'blogs.html',data)    