from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60)(NewsList.as_view())),
    path('search/', NewsSearchList.as_view()),
    path('<int:pk>', cache_page(300)(NewsDetail.as_view())),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('categories/<int:pk>/', PostCategoryList.as_view(), name='post_category'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]

