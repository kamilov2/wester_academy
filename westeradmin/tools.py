from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.shortcuts import redirect

from django.contrib.auth.models import User

from django.http import HttpResponse


def deco_login(request):
    if request.user.is_authenticated:
        user_exists = User.objects.filter(username=request.user.username).exists()
        return user_exists
    else:
        return False





def login_(username , password):
   

    if username and password:
        user = authenticate(username=username, password=password)

        if user is not None:
            login(username, password)
            return redirect("westeradmin:students")
        else:
            return HttpResponse('Неправильное имя пользователя или пароль')
    else:
        return HttpResponse('Отсутствует имя пользователя или пароль')