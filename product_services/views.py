from django.http import JsonResponse
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . import models
from home.models import Footer
from django.core.paginator import Paginator
from . import forms
from django.views.generic.edit import FormMixin

from .models import Product, Like

categories = models.Category.objects.all()


# def detail(request, id):
#     products = models.Product.objects.get(id=id)
#     footer = Footer.objects.first()
#     phone = footer.phone_number
#
#     if request.method == 'POST':
#
#         form = forms.CommentForm(request.POST)
#
#         if form.is_valid():
#             user = form.cleaned_data.get('user')
#             text = form.cleaned_data.get('text')
#
#             models.Comment.objects.create(user=user, text=text, product=products)
#
#             form = forms.CommentForm
#
#     else:
#         form = forms.CommentForm
#
#     return render(request, 'product_services/detail.html', context={
#         'product': products,
#         'categories': categories,
#         'form': form,
#         'phone': phone,
#
#     }
#                   )


class ProductDetailView(FormMixin, DetailView):
    model = models.Product
    form_class = forms.CommentForm
    template_name = 'product_services/detail.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'id': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        user = self.request.user
        text = form.cleaned_data.get('text')

        models.Comment.objects.create(user=user, text=text, product=self.object)
        return super(ProductDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.CommentForm
        context['phone'] = Footer.objects.first().phone_number
        context['categories'] = models.Category.objects.all()
        if self.request.user.is_authenticated:
            if self.request.user.likes.filter(product_id=self.object.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False

        return context


# def products_list(request):    i prefer to use class base views but the function base views are still usefull some where! and i just comment theme not remove.
#     all_products = models.Product.objects.all()
#     pagination = Paginator(all_products, 6)
#     page_number = request.GET.get('page')
#     products = pagination.get_page(page_number)
#
#     return render(request, 'product_services/product_list.html', context={'products': products})


# def services_list(request):
#     services = models.Service.objects.all()[:6]
#
#     return render(request, 'product_services/service_list.html', context={'services': services})

class ServicesListView(ListView):
    model = models.Service


# def category_list(request, pk):
#     category = models.Category.objects.get(id=pk)
#     products = category.products.all()
#     pagination = Paginator(products, 6)
#     page_number = request.GET.get('page')
#     products = pagination.get_page(page_number)
#
#     return render(request, "product_services/product_list.html", context={'products': products})


class CategoryListView(ListView):
    model = models.Product
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        query = super().get_queryset()

        query = query.filter(category=self.kwargs['pk'])
        return query


# def service_detail(request, pk):


#     service = models.Service.objects.get(id=pk)
#
#     return render(request, 'product_services/detail.html', context={"product": service})

class ServiceDetailView(DetailView):
    model = models.Service
    context_object_name = 'product'
    template_name = 'product_services/detail.html'


# def search_list(request):
#     search = request.GET.get('search')
#     result = models.Product.objects.filter(title__icontains=search)
#     pagination = Paginator(result, 6)
#     page_number = request.GET.get('page')
#     products = pagination.get_page(page_number)
#
#     return render(request, 'product_services/product_list.html', context={'products': products})

class SearchView(ListView):
    model = models.Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(title__icontains=self.request.GET.get('search'))
        return query


class ProductListView(ListView):
    model = models.Product
    context_object_name = 'products'
    paginate_by = 6


def like(request, product_id):
    try:
        like_object = models.Like.objects.get(product_id=product_id, user_id=request.user.id)
        like_object.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        models.Like.objects.create(product_id=product_id, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})


