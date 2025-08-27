from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('-published_at')
    scope = Scope.objects.all()
    context = {
        'object_list' : object_list,
        'scope' : scope
    }
    return render(request, template, context)
