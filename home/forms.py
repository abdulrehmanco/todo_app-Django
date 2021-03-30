from django import forms
from .models import *
from django.forms import ModelForm

class formtodo(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new Task...'}))
    
  class Meta:
      model = todoform
      fields = '__all__'
