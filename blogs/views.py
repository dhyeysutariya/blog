from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category, Comment
from django.db.models import Q

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
    if request.method == 'POST':
        comment=Comment()
        comment.user=request.user
        comment.blog=blog
        comment.comment=request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    comments=Comment.objects.filter(blog=blog)
    data={
        'blog':blog,
        'comments':comments
    }
    return render(request,'blogs.html',data)    

def search(request):
    keyword= request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')
    data={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',data)