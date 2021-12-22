from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='pizza-home'),
    path('pizza_cart/', views.cart, name='pizza-cart'),
    path('pizza_contacts/', views.contacts, name='pizza-contacts'),
    path('pizza_about/', views.about, name='pizza-about'),
    path('pizza_menu/', views.menu, name='pizza-menu'),
    path('add_to_cart/<food_id>/', views.add_to_cart, name='add_to_cart')

]
