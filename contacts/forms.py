from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ContactForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'comments')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'comments': 'Comments',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    username = forms.CharField(
        required=True,
        label='Username', 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True, 
        label='Email',
        help_text='Required. Enter a valid email address.', 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        required=True, 
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Your password must contain at least 8 characters.')
    password2 = forms.CharField(
        required=True, 
        label='Password confirmation', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
        help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Password confirmation',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        required=True, 
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True, 
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')