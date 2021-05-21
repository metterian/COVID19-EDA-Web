from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def ex1(request):
    return render(request, 'ex1.html', {})    

def ex2(request):
    return render(request, 'ex2.html', {})    