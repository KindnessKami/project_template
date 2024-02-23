from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def we_do(request):
    return render(request, 'we_do.html')


def contact(request):
    return render(request, 'contact.html')
