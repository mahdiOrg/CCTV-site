from django.shortcuts import render
from product_services import models as product_models
from . import models as home_models
from article import models as article_models
from django.views.generic import TemplateView


# def home(request):
#     products = product_models.Product.objects.all()
#     about = home_models.AboutUS.objects.first()
#     new_products = product_models.Product.objects.order_by('-add_time')[:6]
#     services = product_models.Service.objects.all()[:6]
#     articles = article_models.Article.objects.all()[:2]
#
#     return render(request, 'home/homePage.html', context={
#         'about': about,  # about_us
#         'new_products': new_products,
#         'services': services,
#         'articles': articles,
#     })


class HomeView(TemplateView):
    template_name = 'home/homePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = product_models.Product.objects.all()
        context['about'] = home_models.AboutUS.objects.first()
        context['new_products'] = product_models.Product.objects.order_by('-add_time')[:6]
        context['services'] = product_models.Service.objects.all()[:6]
        context['articles'] = article_models.Article.objects.all()[:2]
        return context
