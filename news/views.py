from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import *
from django.contrib.auth.models import User

from .models import Article

def home(request):
    return redirect('articles')



class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    context_obejct_name = "article"


def reporter(request, username):
    reporter = get_object_or_404(User, username=username)
    context = {
        'reporter': reporter
    }
    return render(request, 'news/reporter.html', context)