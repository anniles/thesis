from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserProfileForm, UserForm
from .models import UserProfile

from booking.models import Booking, BookingItem


# Create your views here.

@login_required
def avatar(request):
    
    user = request.user
    
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
    
    user = request.user

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

@login_required
def bookings(request):

    user = request.user
    bookings = Booking.objects.filter(user=user).all()

    context = { 
        'bookings': bookings,
    }

    return render(request, 'user_profile/bookings.html', context)

@login_required
def bookingItems(request, id):

    user = request.user
    booking = Booking.objects.get(pk=id)

    context = { 
        'booking': booking,
    }

    return render(request, 'user_profile/booking.html', context)