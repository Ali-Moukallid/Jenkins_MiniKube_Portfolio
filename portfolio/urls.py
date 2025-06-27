from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('current-work/', views.current_work, name='current_work'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
] 