from django.urls import path, include
from . import views

urlpatterns = [
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
    path('listings/', views.listing, name='listing')

    # path('forms/product/', views.submit_product),
    # path('forms/request/', views.submit_request),
]
