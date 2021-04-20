from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        
        #yeni ekleme baslangic
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        #yeni ekleme son
        
        password = form.cleaned_data.get('password')

        #newUser = User(username=username)
        newUser = User(username=username,first_name=first_name,last_name=last_name,email=email)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        #messages.info(request, 'Basari ile kayit oldunuz...')
        messages.info(
            request, f'Sn. {first_name} {last_name} basari ile kayit oldunuz...')

        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


""" Bu Şekilde de çalışıyor
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            newUser = User(username = username)
            newUser.set_password(password)
            
            newUser.save()
            login(request,newUser)
            
            return redirect('index')
        context = {
            'form' : form
        }
        return render(request,'register.html',context)    
            
            
    else:
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request,'register.html',context)"""


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        

        user = authenticate(username=username, password=password)
        
        
        if user is None:
            messages.info(request, 'Kullanici Adi veya Parola yanlis')
            return render(request, 'login.html', context)

        #messages.success(request, 'Basari ile giris yaptiniz')
        messages.success(
            request, f'Sn. {user.first_name} {user.last_name} basari ile giris yaptiniz...')
        login(request, user)
        return redirect('index')

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'Basari ile cikis yaptiniz')
    return redirect('index')
