from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('login/', auth_views.login_view),
    path('register/', auth_views.register_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('about/', views.about),


]
