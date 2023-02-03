from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login_form, name = 'login'),
    path('logout/', views.logout_form, name = 'logout'),
]



