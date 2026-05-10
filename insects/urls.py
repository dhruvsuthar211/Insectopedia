from django.urls import path
from . import views

urlpatterns = [
    #The Home Page & Search
    path('', views.home_view, name='home'),
    path('live-search/', views.live_search, name='live_search'),
    
    #All Orders (The Explore Page)
    path('explore/', views.order_list_view, name='order_list'),
    
    #Families within an Order
    path('order/<slug:order_name>/', views.family_list_view, name='family_list'),
    
    #Species within a Family
    path('family/<slug:family_slug>/', views.species_grid_view, name='species_grid'),

    #The Individual Insect Profile
    path('insect/<slug:slug>/', views.InsectDetailView.as_view(), name='insect_detail'),
]