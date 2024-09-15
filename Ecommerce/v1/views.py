from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def shop(request):
    return render(request,"shop.html")
def cart(request):
    return render(request,"cart.html")
def sell(request):
    return render(request,"sell.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")