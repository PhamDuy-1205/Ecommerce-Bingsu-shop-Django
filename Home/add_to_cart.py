# Add Library
from django.shortcuts import render,redirect
from django.views import View
from Category.models import Category
from Product.models import Product




# Code
class add_to_cart(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('cart')    #Load lại trang html, redirect('cart'): load lại page có name = cart ở Home/url
    
    
    def get(self,request):
        cart = request.session.get('cart')
        products = Product.get_all_products()
        if not cart:
            request.session['cart'] = {}
        return render(request,'Home/add_to_cart.html',{'cart':cart, 'products':products})





