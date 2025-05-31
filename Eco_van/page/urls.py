from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/dashboard_new/', views.admin_dashboard, name='admin_dashboard_new'),
    
    
]