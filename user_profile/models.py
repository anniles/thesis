from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    home_address = models.CharField(max_length=50, blank=True)
    phone_numer = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

        