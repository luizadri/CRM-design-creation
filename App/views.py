from django.shortcuts import render

# Create your views here.

def HomePage(request):

    return render(request, 'Home.html')

def SamplePage(request):

    return render(request, 'Sample.html')
