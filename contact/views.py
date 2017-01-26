from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader

# for email imports
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from django import template
from django.contrib import messages
from .forms import ContactForm


# make it whith function
# def contact(request):
#     template = loader.get_template('contact/index.html')


#     return  HttpResponse(template.render())

def thanks(request):
    template = loader.get_template('contact/thanks.html')


    return  HttpResponse(template.render())


# our view
def contact(request):
    form_class = ContactForm

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = form_class(data=request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            contact_name = request.POST.get('fname', '')
            contact_lname = request.POST.get('lname', '')
            contact_email = request.POST.get('email', '')
            contact_phone = request.POST.get('phone', '')
            # contact_message = request.POST.get('message', '')
            form_content = request.POST.get('message', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_lname': contact_lname,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                # 'contact_message': contact_message,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission", 
                content, "Kavala Guide" +'', 
                ['anniles_@hotmail.com'], 
                headers = {'Reply-To': contact_email }
                )
            email.send()
            
            p = form.save()

            messages.success(request, 'Thank you for your message!')
            form = ContactForm()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contact:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form, 'active_tab':'contact'})
