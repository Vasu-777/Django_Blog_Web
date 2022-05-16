from django import forms
from .models import Contact,Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'email','subject','message']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model=Subscriber  
        fields=['email']      