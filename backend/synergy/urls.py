from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'businesses', views.BusinessView, basename='Business')

urlpatterns = [
    path(
        'accounts/login/',
        views.CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name='synergy/login.html'
        ),
        name='login'
    ),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('forms/product/', views.submit_product),
    path('home/', views.home, name='home'),
    path('listings/', views.listing, name='listing'),
]
