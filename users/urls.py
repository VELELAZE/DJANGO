
from django.urls import path
from . import views

#from views import display

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.dashboard,name='profile'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout, name='logout'),
    path('data/',views.db_queries),
]