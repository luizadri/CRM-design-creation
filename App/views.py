from django.shortcuts import render

# Create your views here.

def HomePage(request):

    return render(request, 'Home.html')


def PricePage(request):

    return render(request, 'Price.html')


def hidden(request):

    return render(request, 'Archived.html')




