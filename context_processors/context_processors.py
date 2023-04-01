from product_services import models
from article import models as art_models
from home.models import Footer


def recent_products_c(request):
    recent_products = models.Product.objects.order_by('-add_time')[:3]

    return {"recent_products_c": recent_products}


def all_categories_c(request):
    all_categories = models.Category.objects.all()

    return {"all_categories_c": all_categories}


def recent_articles_c(request):
    recent_articles = art_models.Article.objects.order_by('-add_time')[:3]

    return {"recent_articles_c": recent_articles}


def footer(request):
    footer = Footer.objects.all()[:1]

    return {'footer':footer}
