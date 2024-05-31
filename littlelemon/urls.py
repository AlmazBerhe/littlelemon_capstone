"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from restaurant import views
from rest_framework import routers
from restaurant.views import BookingViewSet
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('login')

router = routers.DefaultRouter()
router.register(r'restaurant/users', views.UserViewSet)
router.register(r'restaurant/booking/tables', views.BookingViewSet, basename="booking")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include(router.urls)),
    path('restaurant/booking/tables/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='book'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    
    # note: remove duplicated url for login. Use either accounts/login or login
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    
]
