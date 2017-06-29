from django import forms

from .models import Post
#from django.forms import ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'email','genre', 'academic_subject',
                  'year', 'price', 'phone_number', 'additional_comments')
