from django.urls import path
from website import views as webpages
from accounts import views as authpages
urlpatterns = [
    path('', webpages.index, name='index'),
    path('homePage/', webpages.home, name='home'),
    path('itemsPage/', webpages.items, name='items'),
    path('dashboard/', webpages.dashboard, name='menu'),

    path('login/', authpages.loginPage, name='login'),
    path('register/', authpages.registerPage, name='register'),
    path('logout/', authpages.logoutUser, name='logout'),
]