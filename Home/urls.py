from django.urls import path
from Home import views
from .add_to_cart import add_to_cart

urlpatterns = [
    path('', views.Index, name = 'home'),
    path('cart/', add_to_cart.as_view(), name = 'cart'),
    path('contact/', views.contact, name = 'contact'),
    path('checkout/', views.checkout, name = 'checkout'),
]



