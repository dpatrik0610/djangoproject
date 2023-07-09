from django.urls import path
from website import views as webpages

urlpatterns = [
    path('', webpages.index, name='index'),
    path('homePage/', webpages.home, name='home'),
    path('itemsPage/', webpages.items, name='items'),
    path('menuPage/', webpages.menu, name='menu'),
]