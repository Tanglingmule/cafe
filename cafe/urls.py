from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuListView.as_view(), name='menu'),
    path('menu/add/', views.MenuItemCreateView.as_view(), name='add_menu_item'),
    path('menu/<int:pk>/edit/', views.MenuItemUpdateView.as_view(), name='edit_menu_item'),
    path('success/', views.success_view, name='success'),
    path('order/create/', views.create_order, name='create_order'),
]
