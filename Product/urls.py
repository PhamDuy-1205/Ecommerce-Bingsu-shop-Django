from django.urls import path
from Product import views

urlpatterns = [
    path('<int:categoryId>', views.getProductByCategory, name = 'getProductByCategoryId'),
    path('detail/<int:productId>', views.detailProduct, name = 'ProductDetail'),
    path('special-offer', views.special_offer, name = 'special_offer'),
]