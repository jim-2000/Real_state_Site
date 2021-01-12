from django.urls import path
from . import views



urlpatterns = [
     path('', views.index, name = "Home"),
     path('home/<int:id>/', views.home , name = "Know"),
     path('contact/', views.contact , name = "Contact"),
     path('services/', views.service, name = "Service"),
     path('about/', views.about, name = "About"),
     path('project/<int:id>/', views.singel_post, name = "SingelProject")
]