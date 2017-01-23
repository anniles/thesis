from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfileForm, UserProfile, UserForm
from django.contrib.auth.models import User


# Create your views here.

@login_required
def avatar(request):
    
    user = User.objects.get(username=request.user.username)
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'picture': userprofile.picture, 'home_address': userprofile.home_address, 'phone_numer': userprofile.phone_numer})
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('user_profile:avatar')
        else:
            print(form.errors)
    
    return render(request, 'user_profile/avatar.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form})

@login_required
def profile(request):
    
    user = User.objects.get(username=request.user.username)
    form = UserForm({
        'first_name': user.first_name,
        'last_name': user.last_name,
        })
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('user_profile:profile')
        else:
            print(form.errors)
    
    return render(request, 'user_profile/profile.html',
        {'selecteduser': user, 'form': form})