from django.shortcuts import render
from backend.models.products import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    search = request.GET.get("keywords")
    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
        search = ""    
    context = {"products":products, "search":search}
    return render(request, 'index.html', context)

def signIn(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request, 'register.html')    