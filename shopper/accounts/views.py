from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only

#Start of user registration function
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            messages.success(request, 'Account was created for:' + "" + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
#End of user registration function

#Start of user Login page function
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)
#End of user Login page function

#Start of user Login page function
def logoutuser(request):
    logout(request)
    return redirect('login')
#End of user Login page function

#Start of user function
def customer(request, pk_test):
    customer = Customers.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/user.html', context)
#End of user function

#Start of Dashboard function
@login_required(login_url='register')
#@admin_only
def accounts(request):
   orders = Order.objects.all()
   customers = Customer.objects.all()
   total_customers = customers.count()
   total_orders = orders.count()
   delivered = orders.filter(status='Delivered').count()
   pending = orders.filter(status='Pending').count()
   context = {'orders': orders, 'users': customers, 'total_orders': total_orders, 'delivered': delivered,
   'pending': pending}
   return render(request, 'accounts/dashboard.html', context)
#End of Dashboard function

#Start of Dashboard function
def page(request):
   products = Product.objects.all()
   users = User.objects.all()
   total_users = users.count()
   total_products = product.count()
   context = {'products': products, 'users': users, 'total_orders': total_orders}
   return render(request, 'accounts/product.html', context)

#Start of Shopping List function
def list(request):
   orders = Order.objects.all()
   return render(request, 'accounts/view_list.html', {'orders':orders})
#End of Shopping List function

#Start of Item in List form
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

#Start of Creating Shopping List function
@login_required(login_url='login')
def createOrder(request, pk):
    customer = Customer.objects.get()
    form = OrderForm(initial={'customer':customer})
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
#End of Creating Shopping List function

#Start of Adding Item into Shopping category and List function
@login_required(login_url='login')
def addList(request, pk):
    order = Order.objects.get(id=pk)
    order = Order.objects.add(order)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
#End of Adding Item into Shopping List category and function

#Start of Update/Editing Item into Shopping category and List function
@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
#Start of Update/Editing Item into Shopping category and List function

#Start of Deleting Item in Shopping category and List function
@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
#End of Deleting Item in Shopping category and List function









