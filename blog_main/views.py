from django.shortcuts import redirect, render
from assignments.models import About, SocialLink
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .forms import RegistrationForm
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

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)

    form=RegistrationForm()
    data={
        'form':form
    }
    return render(request,'register.html',data)

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')

    form=AuthenticationForm()
    data={
        'form':form
    }
    return render(request,'login.html',data)

def logout(request):
    auth.logout(request)
    return redirect('home')