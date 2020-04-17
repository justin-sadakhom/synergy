from django.urls import path
from . import views

urlpatterns = [
    path('forms/product/', views.submit_product),
    path('forms/request/', views.submit_request),
    path('register/', views.sign_up),
    path('success/', views.success, name='success'),
]
