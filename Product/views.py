from django.shortcuts import render,redirect
from Product.models import Product
from django.views import View

# Create your views here.

def getProductByCategory(request, categoryId):
    lstProduct = Product.objects.filter(CategoryId = categoryId)
    Find_Product = Product.objects.all()
    data = {}
    data['lstProduct'] = lstProduct
    data['Find_Product'] = Find_Product
    return render(request, 'Product/ListProduct.html', data)


def detailProduct(request, productId):
    detailProduct = Product.objects.get(pk = productId)
    return render(request, 'Product/DetailProduct.html', {'detailProduct':detailProduct})


def special_offer(request):
    return render (request,'Product/special_offer.html')


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
        print('ProductDetail',request.session['cart'])
        return redirect('ProductDetail')   
    
    
    def get(self,request):
        cart = request.session.get('cart')
        products = Product.get_all_products()
        if not cart:
            request.session['cart'] = {}
        return render(request,'Product/DetailProduct.html',{'cart':cart, 'products':products})