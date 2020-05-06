from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # path('forms/product/', views.submit_product),
    # path('forms/request/', views.submit_request),
    path('home/', views.home, name='home'),
    path('accounts/login/', views.CustomLoginView.as_view(redirect_authenticated_user=True, template_name='synergy/register.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
