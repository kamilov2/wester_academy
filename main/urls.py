from django.urls import path
from .views import *
app_name = "main"

urlpatterns = [
    path("" , HomePageView.as_view() , name ="home"),
    path('create_student' , CreateStudentView.as_view() , name="create_student"),
    path('consulting' , ConsultingView.as_view() , name="consulting")
]