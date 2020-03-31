from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.submit_product),
    path('request/', views.submit_request),
    path('signup/', views.signup),
]
