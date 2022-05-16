# from django_summernote.widgets import  SummernoteInplaceWidget,SummernoteWidget #widgets
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField #fields
from django import forms
from django.forms import EmailInput,TextInput
from django.forms.widgets import Textarea
from .models import Post,Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=SummernoteWidget())
    # content = SummernoteTextField()
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 30}))
    is_published = forms.BooleanField(label="Publish")
    class Meta:
      model=Post
      fields=('title','category','content','image','is_published')
      # widgets={
      #   'content':forms.ChoiceField()
      # }

class CommentForm(forms.ModelForm): 
 
  class Meta:
    model = Comment
    fields=('body',)  
    labels={'body':'Comment'}  
    widgets = {
            'body':Textarea(
              attrs={
              "placeholder":"Enter your comment here",
              "style":"background-color:white;",
              "rows":6,
              
              }
              
            )
        }