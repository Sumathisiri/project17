from django.shortcuts import render

# Create your views here.


def first(request):
    return render(request,'app1.html')


def second(request):
    return render(request,'app2.html')

def third(request):
    return render(request,'app3.html')

def fourth(request):
    return render(request,'app4.html')
    
