from django import forms

from .models import Post
from .models import SearchForm
from django.contrib.auth.models import User
#from django.forms import ModelForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'email','genre', 'academic_subject',
                  'year', 'price', 'phone_number', 'additional_comments')

class SearchForm(forms.ModelForm):

    class Meta:
        model = SearchForm
        fields = ('search_attribute', 'search_field')

class AdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email','password')
