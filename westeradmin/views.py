from django.shortcuts import render,redirect
from .tools import *
from django.views import View
from django.contrib.auth import authenticate, login , logout
from main.models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('westeradmin:students')
            else:
                error_message = 'Неправильное имя пользователя или пароль'
                return render(request, self.template_name, {'error_message': error_message})
        
        return render(request, self.template_name, {'error_message': 'Отсутствует имя пользователя или пароль'})
    
    
class StudentView(View):
    @method_decorator(login_required(login_url='westeradmin:login'))
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:        
            students = RegisterStudent.objects.all()            
            context = {
                "student": students
            }
            
            return render(request, "admin.html", context)
       
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('westeradmin:login')
    
class StatusView(View):
    def get(self, request , pk):
        user_id = pk
        print(user_id)
        my_object = get_object_or_404(RegisterStudent, id=user_id)

        my_object.status = True
        my_object.save()
        print(my_object.status)

        return redirect('westeradmin:students')
    



    