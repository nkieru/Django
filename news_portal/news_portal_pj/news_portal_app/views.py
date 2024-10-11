from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django_filters.rest_framework import FilterSet
from django.core.cache import cache

from .models import *
from .filters import PostFilter
from .forms import NewsForm, ArticleForm

import pytz
from django.shortcuts import redirect
from django.utils import timezone


class NewsList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_len'] = Post.objects.all()
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        # context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news')

class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request, *args, **kwargs):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news/' + str(self.kwargs['pk']))

    # def get_object(self, *args, **kwargs):
    #     obj = cache.get(f'post-{self.kwargs["pk"]}', None)
    #     if not obj:
    #         obj = super().get_object(queryset=self.queryset)
    #         cache.set(f'post-{self.kwargs["pk"]}', obj)
    #     return obj



class NewsSearchList(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_len'] = Post.objects.all()
        context['filterset'] = self.filterset
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news/search/')


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal_app.add_post')
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.type = 'N'
        news.author = self.request.user.author
        return super().form_valid(form)


class ArticleCreate(CreateView):
    permission_required = ('news_portal_app.add_post')
    form_class = ArticleForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'A'
        article.author = self.request.user.author
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_portal_app.change_post')
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


# class ArticleEdit(LoginRequiredMixin, UpdateView):
#     form_class = ArticleForm
#     model = Post
#     template_name = 'article_edit.html'


class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_portal_app.change_post')
    form_class = ArticleForm
    model = Post
    template_name = 'article_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = '/news/'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = '/news/'


class PostCategoryList(NewsList):
    model = Post
    ordering = '-date_time'
    template_name = 'category.html'
    context_object_name = 'category_list'
    paginate_by = 10

    def get_queryset(self):
        self.categories = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories=self.categories)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.categories.subscribers.all()
        context['categories'] = self.categories
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    categories = Category.objects.get(id=pk)
    categories.subscribers.add(user)
    message = _('You have subscribed to the category: ')
    return render(request, 'subscribe.html', {'categories': categories, 'message': message})





