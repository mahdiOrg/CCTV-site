from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator
from . import forms
from django.http import HttpResponseRedirect
from django.views.generic import ListView


# def article(request):
#     articles = models.Article.objects.all()
#     paginator = Paginator(articles, 3, )
#     page_number = request.GET.get('page')
#     articles_list = paginator.get_page(page_number)
#
#     return render(request, 'article/article_list.html', context={'articles': articles_list})

class ArticleListView(ListView):
    model = models.Article
    context_object_name = 'articles'
    paginate_by = 3


def article_detail(request, id):
    article = models.Article.objects.get(id=id)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('user')
            text = form.cleaned_data.get('text')

            models.Comment.objects.create(user=user, text=text, article=article)
            form = forms.CommentForm

    else:
        form = forms.CommentForm
    return render(request, 'article/article_detail.html', context={'article': article,
                                                                   'form': form, })
