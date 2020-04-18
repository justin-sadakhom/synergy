from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('forms/product/', views.submit_product),
    path('forms/request/', views.submit_request),
    path('register/', views.sign_up),
    path('success/', views.success, name='success'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home')
]
