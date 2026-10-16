from django.shortcuts import render

def login(request):
    return render(
        request,
        'projectoup/home.html'
    )


def logout(request):
    return render(
        request,
        'projectoup/home.html'
    )

def profile(request):
    return render(
        request,
        'projectoup/home.html'
    )
