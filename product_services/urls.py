from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('detail/<int:id>', views.ProductDetailView.as_view(), name="detail"),
    path('', views.ProductListView.as_view(), name="products_list"),
    path('service/', views.ServicesListView.as_view(), name="service"),
    path('category/<int:pk>', views.CategoryListView.as_view(), name="category_list"),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name="service_detail"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('like/<int:product_id>', views.like, name='like')
]
