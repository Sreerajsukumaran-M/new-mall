from django import forms
from django.contrib.auth.models import User
from .models import Store

class StoreForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Store
        fields = ['name', 'category', 'username', 'password']