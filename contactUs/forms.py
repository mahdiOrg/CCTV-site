from django import forms
from . import models
from django.core.validators import ValidationError


class MessageForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'موضوع', 'style': "height: 55px;text-align: right",
               'class': 'form-control border-0 px-4'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام', 'style': "height: 55px;text-align: right",
               'class': 'form-control border-0 px-4'}))
    phone = forms.DecimalField(max_digits=11, decimal_places=0,
                               widget=forms.TextInput(
                                   attrs={'placeholder': '9123456789 ', 'style': "height: 55px;text-align: right",
                                          'class': 'form-control border-0 px-4'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control border-0 px-4 py-3','placeholder':'پیام شما یا محصول درخواستی','style':'text-align: right;'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(str(phone)) < 10:
            raise ValidationError('شماره تلفن معتبر نیست')
        elif not str(phone).startswith('9'):
            raise ValidationError('شماره تلفن معتبر نیست')
        else:
            return phone
