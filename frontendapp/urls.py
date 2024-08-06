from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('buynow/', views.buynow,name="buynow"),
    path('bat/', views.bat,name="bat"),
    path('pulses/', views.pulses,name="pulses"),
    path('cards/', views.cards,name="cards"),
    path('cart/', views.cart,name="cart"),
    path('dryfruits/', views.dryfruits,name="dryfruits"),
    path('saffron/', views.saffron,name="saffron"),
    path('food/', views.food,name="food"),
    path('test/', views.test,name="test"),
    
]