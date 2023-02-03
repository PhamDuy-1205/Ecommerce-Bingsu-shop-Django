from django.urls import path
from Category import views

urlpatterns = [
    path('', views.Index, name = ''),

]
