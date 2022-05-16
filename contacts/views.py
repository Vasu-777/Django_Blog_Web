from django.shortcuts import render, redirect
from .forms import SubscriptionForm, ContactForm
from django.contrib import messages
from .models import Contact


# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            # try:
            # if request.method == 'POST':
            #     name=request.POST.get('name')
            #     email=request.POST.get('email')
            #     subject=request.POST.get('subject')
            #     message=request.POST.get('message')
            #     contact=Contact.objects.create(name=name,email=email,subject=subject,message=message)
            #     contact.save()
            messages.info(
                    request, 'We have received your Enquiry.We will contact you shortly')
            return redirect('contact')
            # except:
            #     messages.error(request, 'Something went wrong !')   
            #     return redirect('contact')
    else:
        return render(request, 'contact/contact.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have successfully subscribed to our newsletter!")
            return redirect('index')
