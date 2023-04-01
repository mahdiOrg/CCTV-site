from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles_list'),
    path('detail/<int:id>', views.article_detail, name='article_detail'),
]
