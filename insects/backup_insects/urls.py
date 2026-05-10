from django.urls import path
from . import views

urlpatterns = [
    path('', views.InsectListView.as_view(), name='insect_list'),
    path('insect/<int:pk>/', views.InsectDetailView.as_view(), name='insect_detail'),
]