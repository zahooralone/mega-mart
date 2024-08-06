from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "frontend/pages/home.html")

def pulses(request):
    return render(request, "frontend/pages/pulses.html",)
   
def buynow(request):
    return render(request, "frontend/pages/buynow.html",)
  
def bat(request):
    return render(request, "frontend/pages/bat.html",)
       
def cards(request):
    return render(request, "frontend/pages/cards.html",)
       
def cart(request):
    return render(request, "frontend/pages/cart.html",)
       
def dryfruits(request):
    return render(request, "frontend/pages/dryfruits.html",)
       
def food(request):
    return render(request, "frontend/pages/food.html",)
       
def test(request):
    return render(request, "frontend/pages/test.html",)
       
def saffron(request):
    return render(request, "frontend/pages/saffron.html",)