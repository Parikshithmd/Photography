from django.urls import path
from app import views

urlpatterns = [
    path('',views.Home,name="Home"),
    
    path('contact',views.contact,name="contact"),
    path('Home',views.Home,name="Home"),
   
    path('gallery',views.gallery,name="gallery"),
    path('karnataka',views.karnataka,name="karnataka"),
    path('kerala',views.kerala,name="kerala"),
    path('tamilnadu',views.tamilnadu,name="tamilnadu"),
    path('maharashtra',views.maharashtra,name="maharashtra"),





    
]
