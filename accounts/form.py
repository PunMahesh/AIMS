from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, GENDER_CHOICES
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        label="Create password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Re-enter your password",
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your email address",
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your first name",
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name",
                "class": "form-control"
            }
        )
    )
    contact = forms.IntegerField(
        label="Contact number",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your contact number",
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your address",
                "class": "form-control"
            }
        )
    )

    gender = forms.ChoiceField(
        label="Gender",
        widget=forms.RadioSelect(
            attrs={
                "class": "form-control"
            }
        ),
        choices=GENDER_CHOICES,
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'contact', 'address', 'gender')
