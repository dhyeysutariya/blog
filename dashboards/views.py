from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category
from dashboards.forms import CategoryForm


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