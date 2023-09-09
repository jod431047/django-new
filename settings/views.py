from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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


@login_required
def profiluser(request):
    user_profile = request.user.user_profile

    # Retrieve the profile fields
    bio = user_profile.bio
    profile_picture = user_profile.profile_picture
    address = user_profile.address
    code = user_profile.code

    # Add other fields you want to retrieve

    return render(request, 'settings/profil_user.html', {
        'bio': bio,
        'profile_picture': profile_picture,
        'address': address,
        'code': code,
        # Add other fields you want to pass to the template
    })