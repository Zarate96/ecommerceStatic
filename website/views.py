from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})

def blog(request):
    return render(request, 'website/blog.html', {})

def blogDetails(request):
    return render(request, 'website/blog-details.html', {})
