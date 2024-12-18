"""
URL configuration for web_services_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from .views import RegisterView, LoginView
from .views import ClientMeView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('clients/',views.client_list),
    path('client/<int:id>/<str:name>/', views.client_detail, name='client_detail'),
    path('client/<int:id>/', views.client_detail1),

    path('reservation/', views.create_reservation, name='create_reservation'),  # For creating a reservation
    path('reservations/', views.get_reservations, name='get_reservations'), 
    path('reservations/<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('voyages/', views.voyage_list, name='voyage_list'),  # Recherche et ajout
    path('voyages/<int:pk>/', views.voyage_detail, name='voyage_detail'),  # Détail, modification, suppression
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/reservations/', views.get_user_reservations, name='user-reservations'),
    path('api/client/me/', ClientMeView.as_view(), name='client_me'),
]
