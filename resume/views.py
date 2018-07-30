# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'base.html')

def profile(request):
    return render(request, 'profile.html')

def education(request):
    return render(request, 'education.html')

def training(request):
    return render(request, 'training.html')

def employment(request):
    return render(request, 'employment.html')

def portfolio(request):
    return render(request, 'portfolio.html')

#def contact(request):
#    return render(request, 'contact.html')

def contact(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['nabirhossain13@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request,'success.html')
    return render(request, "contact.html", {'form': form})

