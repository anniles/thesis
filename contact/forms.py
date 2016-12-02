from django import forms
from .models import Contact


class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    fname = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    lname = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    phone = forms.CharField(label='Phone', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter Phone'}), required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Write your message'}))

    def save(self):
        return Contact.objects.create(fname=self.cleaned_data['fname'], lname=self.cleaned_data['lname'], email=self.cleaned_data['email'], phone=self.cleaned_data['phone'], message=self.cleaned_data['message'])