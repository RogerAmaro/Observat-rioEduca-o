from django import forms
from django.contrib.auth.models import User
from arquivo.models import File

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FileForm(forms.ModelForm):
    
    class Meta:
        model = File
        fields = ["file_name","upload_data","file_data"]

