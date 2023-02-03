from django.shortcuts import render,redirect
from Category.models import Category
from Product.models import Product
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views import View
from django.conf import settings
from django.contrib.auth.decorators import login_required



# Create your views here.

def Index(request):
    data = {}
    category = Category.objects.all()
    product = Product.objects.all()[:8]
    data['category'] = category
    data['products'] = product
    return render(request,'Home/home.html',data)



# def register(request):
#     if request.method == 'POST':
#         response = HttpResponse()
#         response.write("Tài khoản đã đăng kí thành công")
#         Name = request.POST['name']
#         Email = request.POST['email']
#         Password = request.POST['password']
        
#         send_mail(
#             request.POST['name'],
#             'nguyenlong.clone.1998@gmail.com',
#             ['phamduy.law.1205@gmail.com'],
#             fail_silently = False
#         )

#         return response

#     registerForm = register_form()
#     return render(request, "Home/register.html", {"form" : registerForm})



@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_content = request.POST['message-content']
        
        # send email funtion
        send_mail(
            message_subject,
            message_content,
            'nguyenlong.clone.1998@gmail.com',
            [message_email],
            fail_silently = False
            )
        
        
        return render(request,'Home/contact.html',{})
        
        
        
    
    else:
        return render(request,'Home/contact.html',{}) 






@login_required(login_url='login')
def checkout(request):
    carts = request.session.get('cart')
    return render(request,'Home/checkout.html',{'carts':carts})

