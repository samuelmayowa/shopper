from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logoutuser/', views.logoutuser, name="logout"),
    path('', views.accounts, name="home"),
    path('list', views.list, name="list"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('add_list/<str:pk>/', views.addList, name="add_list"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]
