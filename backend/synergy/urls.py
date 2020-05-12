from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # path('forms/product/', views.submit_product),
    # path('forms/request/', views.submit_request),
    path('home/', views.home, name='home'),
    path(
        'accounts/login/',
        views.CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name='synergy/login.html'),
        name='login'
    ),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
