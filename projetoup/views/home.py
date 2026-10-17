
from django.shortcuts import render
from django.conf import settings


def home(request):

    context = {'tag_title': settings.SITENAME}

    return render(
        request,
        'projetoup/home.html',
        context
    )
