from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category
from dashboards.forms import BlogPostForm, CategoryForm
from datetime import datetime
from django.template.defaultfilters import slugify
from uuid import uuid4


@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.count()
    blog_count=Blog.objects.count()
    data={
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',data)

def categories(request):
    categories=Category.objects.all()
    data={
        'categories':categories
    }
    return render(request,'dashboard/categories.html',data)

def add_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    data={
        'form':form,
    }
    return render(request,'dashboard/add_category.html',data)

def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    form=CategoryForm(instance=category)
    data={
        'form':form,
        'category':category
    }
    if request.method == 'POST':
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    return render(request,'dashboard/edit_category.html',data)

def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def blogs(request):
    blogs=Blog.objects.all()
    data={
        'blogs':blogs
    }

    return render(request,'dashboard/blogs.html',data)

def add_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # 1️⃣ temporary unique slug (never empty, never duplicate)
            base = slugify(form.cleaned_data["title"])
            post.slug = f"{base}-{uuid4().hex[:8]}"

            post.save()  # ✅ first save is safe

            # 2️⃣ final human-readable slug using ID
            post.slug = f"{base}-{post.id}"
            post.save(update_fields=["slug"])

            return redirect("blogs")

    return render(request, "dashboard/add_blog.html", {"form": BlogPostForm()})