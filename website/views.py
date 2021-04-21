from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogDetails(request):
    return render(request, 'blog-details.html', {})
