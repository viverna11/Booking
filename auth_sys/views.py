from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'auth_sys/login.html')

def Logout(request):
    logout(request)
    return redirect('room_list')
    