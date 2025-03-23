from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request, store_id):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store_id = store_id
            product.save()
            return redirect('shop_dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})

from django.shortcuts import redirect, get_object_or_404
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('shop_dashboard')


from django.shortcuts import render, get_object_or_404
from store.models import Store
from .models import Product

def product_list(request, store_id):
    store = get_object_or_404(Store, id=store_id)  # Get the selected shop
    products = Product.objects.filter(store=store)  # Get products for the selected shop
    return render(request, 'products/product_list.html', {'store': store, 'products': products})