from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include("inventory_system.urls")),  # Ensure inventory_system has a urls.py
    path('', auth_views.LoginView.as_view(template_name="inventry/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="inventry/logout.html"), name="logout"),
]
