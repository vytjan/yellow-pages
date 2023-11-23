from django.urls import path
from . import views
from .views import login_view, logout_view

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.viewContact, name='viewContact'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]