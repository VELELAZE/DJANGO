from django.contrib import admin
from django.urls import path,include
from users import views as userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.index, name = 'index'),
    path('user/',include('users.urls')),
]
