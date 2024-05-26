from django.urls import path
from .views import *

app_name = "westeradmin"

urlpatterns = [
    path("login" , LoginView.as_view() , name = "login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path("lids/" , StudentView.as_view() , name = "students"),
    path('status/<int:pk>' , StatusView.as_view() , name = "status")
    
]