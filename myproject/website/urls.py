from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homePage/', views.home, name='home'),
    path('itemsPage/', views.items, name='items'),
    path('menuPage/', views.menu, name='menu'),
]