from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('register/',views.register,name='register'),
    path('home/',views.home, name='home'),
    path('products/',views.products,name='products'),
    path('brands/',views.brands,name='brands'),
    path('services/',views.services,name='services'),
    path('orders/',views.orders,name='orders'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('Contactus/',views.Contactus,name='Contactus'),

]