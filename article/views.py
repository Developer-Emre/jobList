from django.shortcuts import render

# Create your views here.

def index (request):
    return render( request,'index.html')

def error (request):
    return render( request,'404.html')

def about (request):
    return render( request,'about.html')

def category (request):
    return render( request,'category.html')

def contact (request):
    return render( request,'contact.html')

def detail (request):
    return render( request,'job-detail.html')

def job (request):
    return render( request,'job-list.html')

def test (request):
    return render( request,'testimonial.html')
