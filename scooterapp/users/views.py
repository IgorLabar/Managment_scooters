from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


#Регистрация пользователя
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})



#Если пользователь зарегестрирован, то может войти со своим логином и паролем
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')