from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseForbidden,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth import get_user_model
from .models import Products
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.db import transaction
User = get_user_model()
def index(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            return HttpResponseForbidden("User does not exist")
        products = Products.objects.all().order_by('-created_at')[:8]
        
        return render(request,"index.html",{"user":user, "products":products})
    return HttpResponseRedirect(reverse('login'))
def shop(request):
    if request.user.is_authenticated:
        products = Products.objects.all().order_by('-created_at')
        paginator = Paginator(products,8)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        return render(request,"shop.html",{"products":products})
    return render(request,"shop.html")

def confirmPurchase(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username) 
        items = user.cart.all()
        with transaction.atomic():
            user.cart.remove(*items)
        messages.success(request, "Bought Successfully")
        return JsonResponse({"message":"success"})
def searchShop(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST.get('search')
            if data:  # Ensure data is not None or empty
                products = Products.objects.filter(name__icontains=data)
                paginator = Paginator(products, 8)
                page_number = request.GET.get('page')
                products = paginator.get_page(page_number)
                return render(request, "shop.html", {"products": products})
            else:
                return render(request, "shop.html", {"products": []})
    return HttpResponseRedirect(reverse('login'))

def cart(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        cart_items = user.cart.all()

        return render(request,"cart.html",{"cart_items":cart_items})

def sell(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            productName = request.POST.get('productName')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category = request.POST.get('category')
            product = Products(
                name = productName,
                description = description,
                price = price,
                created_by = request.user,
                category = category
            )
            product.image = image
            product.save()
            messages.success(request, "Product published Successfully")
            return HttpResponseRedirect(reverse('index'))
        return render(request,"sell.html")
    return HttpResponseRedirect(reverse('login'))
def login(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            errors["error"] = "Username and password are required."   
            return render(request, "login.html", {"errors": errors})
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                errors["error"] = "Invalid credentials."
    
            return render(request, "login.html", {"errors": errors})
    elif request.method == "GET":
        
        if request.user.is_authenticated:
            logout(request)
        if messages.get_messages(request):
            return render(request,"login.html")
        else:
            return render(request,"login.html")

def signup(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        user = User.objects.filter(username=username).first()
        errors = {}
        if user:
            errors["error"] = "User already exists"
        elif not all([username, full_name, password, email, image]):
            errors["error"] = "All fields are required"
        elif len(password) < 8:
            errors["error"] = "Password must be at least 8 characters"
        elif password != confirm_password:
            errors["error"] = "Passwords do not match"
        if errors:
            return render(request, 'signup.html', {"errors": errors})
        user = User(
            username = username,
            full_name = full_name,
            email = email,
        )
        user.image = image
        user.set_password(password)
        user.save()
        messages.success(request, "Registered Successfully")
        return HttpResponseRedirect(reverse("login"))
    return render(request, "signup.html")
@csrf_exempt
def addCart(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(username=request.user.username)
            product = Products.objects.get(id=id)
            user.cart.add(product)
            user.save()
            number = user.cart.count()
            return JsonResponse({"message":True,"number":number})
    return HttpResponseRedirect(reverse('login'))
def cartNumber(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        number = user.cart.count()
        items = user.cart.all()
        subtotal = Decimal('0.00')
        for item in items:
            subtotal+=Decimal(str(item.price))
        return JsonResponse({"number":number,"subtotal":subtotal})
    return JsonResponse({"number":0})
@csrf_exempt
def deleteCart(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(username=request.user.username)
            product = Products.objects.get(id=id)
            user.cart.remove(product)
            return JsonResponse({"message":True})
    return HttpResponseRedirect(reverse('login'))