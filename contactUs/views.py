from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from home.models import Footer
from contactUs.models import Message
from django.core.validators import ValidationError
from . import forms
from django.views.generic import FormView


# def contact(request):
#     if request.method == 'POST':
#         form = forms.MessageForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data.get('title'))
#             # print(form.cleaned_data.get('name'))
#             title = form.cleaned_data.get('title')
#             name = form.cleaned_data.get('name')
#             phone = form.cleaned_data.get('phone')
#             text = form.cleaned_data.get('text')
#             Message.objects.create(text=text, title=title, phone=phone, name=name)
#             form = forms.MessageForm
#             return redirect('home_app:home')
#         else:
#             form = forms.MessageForm
#     else:
#         form = forms.MessageForm
#
#     info = Footer.objects.first()
#     return render(request, 'contactUs/contact.html', {'info': info, 'form': form})


class ContactFormView(FormView):
    template_name = 'contactUs/contact.html'
    form_class = forms.MessageForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        data = form.cleaned_data
        Message.objects.create(**data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Footer.objects.first()
        return context

