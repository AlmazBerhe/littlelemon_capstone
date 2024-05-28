from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]