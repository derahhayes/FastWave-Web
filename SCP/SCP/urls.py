from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from SCP import views
from auth import views as auth_views
from landing import views as landing_views
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path('', landing_views.landing_page_view, name="Home"),
    path('login/', auth_views.login_view),
    path('register/', auth_views.register_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #accounts
    path('about/', views.about),
    path("api/", include(router.urls)),
]