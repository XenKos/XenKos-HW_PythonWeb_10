from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from .models import User, Author, Quote

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Перевірка на наявність користувача з таким email
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no user with this email address.")
        return email

    def save(self, domain_override=None, email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator, request=None, **kwargs):
        super().save(domain_override, email_template_name, use_https, token_generator, request, **kwargs)