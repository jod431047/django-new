from django.shortcuts import render
from products.models import Products
from accounts.models import UserProfile

def home(request):
    products = Products.objects.all()[:12] 
    
    return render(request,'settings/home.html',{'products':products})

def about(request):
    return render(request,'settings/about.html',{})

def testimonial(request):
    return render(request,'settings/testimonial.html',{})

def why(request):
    return render(request,'settings/why.html',{})

def profile(request):
    data = UserProfile.objects.all()
    return render(request,'settings/profile.html',{'data':data})