from django.shortcuts import render, get_object_or_404
from .models import Article




def all_blogs(request):
    articles = Article.objects.order_by('-data')[:5]
    return render(request, 'blog/all_blogs.html', {'articles':articles})

def detail(request, blog_id):
    blog = get_object_or_404(Article, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
