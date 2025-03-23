from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mall.models import Mall
from .models import Store
from .forms import StoreForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def create_store(request, mall_id):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            # Create a User for the shop
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)

            # Create the Store and link it to the User and Mall
            store = form.save(commit=False)
            store.mall_id = mall_id
            store.user = user
            store.save()

            return redirect('mall_dashboard')
    else:
        form = StoreForm()
    return render(request, 'stores/create_store.html', {'form': form})

@login_required
def store_list(request, mall_id):
    mall = get_object_or_404(Mall, id=mall_id)
    stores = Store.objects.filter(mall=mall)
    return render(request, 'stores/store_list.html', {'mall': mall, 'stores': stores})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def shop_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'store'):  # Check if the user is a shop
            login(request, user)
            return redirect('shop_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'stores/shop_login.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product

@login_required
def shop_dashboard(request):
    shop = request.user.store  # Assuming a OneToOneField between User and Store
    products = Product.objects.filter(store=shop)
    return render(request, 'stores/shop_dashboard.html', {'products': products})

def store_logout(request):
    logout(request)
    return redirect('index_dashboard')


from django.shortcuts import render, get_object_or_404
from mall.models import Mall
from .models import Store

def shop_list(request, mall_id):
    mall = get_object_or_404(Mall, id=mall_id)  # Get the selected mall
    shops = Store.objects.filter(mall=mall)  # Get shops for the selected mall
    return render(request, 'stores/shop_list.html', {'mall': mall, 'shops': shops})