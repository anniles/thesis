from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader

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


def contact(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        # print(form)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            messages.success(request, 'Thank you for your message!')
            form = ContactForm()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contact:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})