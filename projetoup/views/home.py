
from django.shortcuts import render
from django.conf import settings
from projetoup.models import Post


def home(request):

    posts = Post.objects.filter(
        is_active=True, is_deleted=False
    ).order_by('-created_at')
    context = {
        'tag_title': f'{settings.SITENAME}',
         'posts': posts
        }
            

    return render(
        request,
        'projetoup/home.html',
        context
    )
