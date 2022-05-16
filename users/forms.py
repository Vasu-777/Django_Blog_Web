from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from captcha.fields import CaptchaField


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=100,label='Phone No.')
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ['username','email','phone','password1', 'password2']
        labels={'username':'Username','email':'Email','phone':'Phone No.','password1':'Password','password2':'Confirm Password'}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['title','skills','image','twitter','instagram'] 
        labels={'twitter':'Twitter Username','instagram':'Instagram Username'}       
