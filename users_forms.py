from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')
    
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


