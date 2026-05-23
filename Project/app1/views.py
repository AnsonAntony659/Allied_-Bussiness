from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'Welcome.html')

def login(request):
    return render(request, 'login.html')

def forgotpassword(request):
    return render(request,  'forgotpassword.html')

def register(request):
    return render(request,'register.html')

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request,'products.html')

def brands(request):
    return render(request,'brands.html')

def services(request):
    return render(request,'services.html')

def orders(request):
    return render(request,'orders.html')


def aboutus(request):
    return render(request,'aboutus.html')

def Contactus(request):
    return render(request,'Contactus.html')