"""fakeproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fakerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Rahul/', views.employee_data),
    path('mainpage/', views.main_page,name='main_page'),
    path('lucknow/',views.Lucknow_employee_data,name='Lucknow'),
    path('gorakhpur/',views.Gorakhpur_employee_data,name='Gorakhpur'),
    path('deoria/',views.Deoria_employee_data,name='Deoria'),
    path('kanpur/',views.Kanpur_employee_data,name='Kanpur'),
    path('register/',views.register_page,name='register'),
    path('',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('feedback/',views.feedback_view,name='feedback'),

]
