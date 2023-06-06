from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import User

class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.MaxLengthValidator(11)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterOtpForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[validators.MaxLengthValidator(11)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self):
    #     phone = self.cleaned_data['phone']
    #     if User.objects.filter(phone__exact=phone).exists():
    #         raise ValidationError({"phone": "تلفن تکراری است"})


class CheckOtpForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])
