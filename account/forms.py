from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data
        else:
            raise ValidationError('اطلاعات وارد شده صحیح نیست!')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_recheck = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):

        if User.objects.filter(username=self.cleaned_data.get('username')).exists():
            raise ValidationError('نام کاربری در حال حاضر وجود دارد یک نام دیگر انتخاب کنید.')
        else:
            return self.cleaned_data.get('username')

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('password_recheck')
        if password != re_password:
            raise ValidationError("گذرواژه ها مطابقت ندارند!")
        else:
            return self.cleaned_data
