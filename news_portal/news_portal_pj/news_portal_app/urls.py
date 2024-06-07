from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('search/', NewsSearchList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
