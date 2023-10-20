from django.shortcuts import render,redirect
from .models import Product,Cart
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login, logout

def product_list(request):
     products = Product.objects.all()
     return render(request,'product_list.html',{'products':products})



def cartlist(request):
    cartproducts = Cart.objects.all()
    return render(request, 'cart_list.html', {'cartproducts': cartproducts})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired home page
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
 return render(request, 'home.html', {'userName': request.user.username})

from .forms import UserRegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})
