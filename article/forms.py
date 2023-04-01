from django import forms


class CommentForm(forms.Form):
    user = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control bg-white border-0 h2',
                                                                         'style': 'height: 55px;width: 100%;text-align: right;',
                                                                         'placeholder': 'نام خود را وارد کنید'}))

    text = forms.CharField(max_length=700, widget=forms.Textarea(attrs={'class': ' form-control bg-white border-0 h1',
                                                                        'placeholder': 'نظر خود را بنویسید ',
                                                                        'style': 'text-align: right;'}))

