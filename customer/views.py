from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def customer_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('customer_login')
    else:
        form = UserCreationForm()
    return render(request, 'customers/customer_register.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')  # Redirect to customer dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'customers/customer_login.html')

from django.contrib.auth.decorators import login_required

@login_required
def customer_dashboard(request):
    return render(request, 'customers/customer_dashboard.html')


def customer_logout(request):
    logout(request)
    return redirect('index_dashboard')